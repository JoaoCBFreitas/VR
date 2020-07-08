from flask import Flask, request, send_from_directory, render_template, redirect, json, url_for, flash
import requests
from pathlib import Path

template_dir = Path(__file__).parent.parent/"Templates"
app = Flask(__name__, template_folder=template_dir)


authContainer = "http://auth:5000"


app.secret_key = 'database'  # TIve um erro que me pediu uma secret key


@app.route('/Logout', methods=['POST'])
def logout():
    data = request.form.to_dict()
    response = requests.post(authContainer + '/logout', data=data)

    return redirect(url_for('index'))


@app.route('/LoggedIn', methods=['GET'])
def loggedIn():
    return render_template('LoggedIn.html')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/Login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        dic = request.form.to_dict()
        print(dic, flush=True)
        # Pedido a API presente no authentication server que trata do processo de login
        response = requests.post(authContainer + '/login', data=dic)
        if response.status_code == 200:
            res = json.loads(response.content)

            flash('Login concluido')
            return redirect(url_for('loggedIn', token=str(res['token']), name=request.form.get('email')))
            print("POST RETURN")
        elif response.status_code == 404:
            error = "Wrong username"
        elif response.status_code == 400:
            error = "Wrong password"
        else:
            error = "Internal error, please contact support"

    return render_template('Login.html')


@app.route('/Registar', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        dic = request.form.to_dict()
        # redirect para o registo da auth_server com as infos do registo
        response = requests.post(authContainer + '/register', data=dic)
        if response.status_code == 200:
            #flash("Registo efetuado")
            print("Registo efetuado")
            return redirect('/Login')
        elif response.status_code == 400:
            error = "Name already taken"
        else:
            error = "Server error, please contact support"
        print(dic)
    return render_template('Registar.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
