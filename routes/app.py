from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!"

@app.route("/hola")
def hola():
    return "Hola"

@app.route("/user/<string:user>")
def user(user):
    return "Hola "+user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {}, Nombre de usuario: {}".format(id, username)

@app.route("/suma/<float:numero_1>/<float:numero_2>")
def suma(numero_1, numero_2):
    return "La suma es: {}".format(numero_1+numero_2)

@app.route("/default/")
@app.route("/default/<string:dft>")
def dft(dft="404"):
    return "El valor default es: "+ dft

if __name__ == "__main__":
    app.run(debug=True)
