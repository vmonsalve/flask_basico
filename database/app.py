from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

dbdir  = "sqlite:///"+os.path.abspath(os.getcwd())+"/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

"""
    Creando tablas de base de datos
    a partir de clases.
"""

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

"""
    Aplicacion.
"""
@app.route("/")
def index():
    titulo = "Bienvenido!"
    lista  = ["Vicente Monsalve", "33", "9 septiembre 1985"]
    return render_template(
            "index.html", 
            titulo=titulo,
            lista=lista
            )
"""
    Insertando datos.
"""
@app.route("/insert/default")
def insert_default():
    new_post = Posts(title="Probando base de datos uno.")
    db.session.add(new_post)
    db.session.commit()
    return "El post por defecto ha sido creado"

"""
    Seleccionando datos.
"""
@app.route("/select/default")
def select_default():
    post = Posts.query.filter_by(id=1).first()
    print(post.title)
    return "El valor ha sido impreso"

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
