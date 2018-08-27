from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Bienvenido!"
    lista  = ["Vicente Monsalve", "33", "9 septiembre 1985"]
    return render_template(
            "index.html", 
            titulo=titulo,
            lista=lista
            )

if __name__ == "__main__":
    app.run(debug=True)
