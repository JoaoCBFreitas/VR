import authentication as auth
from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)
linkHttpApp = "http://http:8080"
linkFtpApp = "http://ftp:5050"


@app.route('/logout', methods=['POST'])
def logout():
    name = request.form.get('email')
    token = request.form.get('token')
    print("\n\n\n"+name+"\n"+token+"\n\n\n", flush=True)
    # verificar se o gajo que pediu para apagar o token tem o token
    if auth.validToken(token, name):
        # apagar o token
        if auth.deleteToken(name):
            return jsonify({"res": "Token deleted"}), 200
        else:
            return jsonify({"res": "Could not delete token"}), 400
    else:
        return jsonify({"res": "Bad token"}), 401


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('email')
    password = request.form.get('psw')

    if not name or not password:
        return redirect(linkHttpApp, code=400)

    if not auth.getUser(name):
        return jsonify({"res": "NO USER"}), 404

    if not auth.verifyPass(name, password):  # retorna true caso seja igual
        return jsonify({"res": "wrong password"}), 400
    token = auth.createToken(name, password)

    data = {'token': token}
    print(data, flush=True)
    return jsonify(data), 200


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('email')
    password = request.form.get('psw')
    result = auth.register(name, password)
    if result == "ok":
        print("Registo funcionou")
        return jsonify({"res": "OK"}), 200
    elif result is not None:
        if result['error'] == "Existing-User":
            return jsonify({"res": "EXISTING USER"}), 400
        elif result['error'] == "Server-Error":
            return jsonify({"res": "SERVER ERROR"}), 500
    else:
        return jsonify({"res": "INTERNAL SERVER ERROR"}),  500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
