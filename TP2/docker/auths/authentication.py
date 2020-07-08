import hashlib
import datetime
import postgres as db  # Criar postgres.py para comunicar com a BD


def verifyToken(token, email):
    if db.existsUser(email):
        print("USER EXISTS")
        if db.verify_Token(email, token):
            print("VALID TOKEN")
            return True
        else:
            print("INVALID TOKEN")
    return False


def getUser(email):
    return db.existsUser(email)


def deleteToken(email):
    print("Deleting Token")
    return db.deleteToken(email)


def createToken(email, password):

    # db.deleteToken(email)

    inputT = email + ":" + password + ":" + str(datetime.datetime.now())
    token = hashlib.sha256(inputT.encode()).hexdigest()

    return token


def register(email, password):
    result = {}
    if not db.existsUser(email):
        result = db.register(email, password)
    else:
        result['error'] = "Existing-User"
    return result


def verifyPass(email, password):
    print("PASS: ", db.getPassword(email), password)
    return db.getPassword(email) == password
