from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# from conexion import conexion, cursor

import os

app = Flask(__name__)

app.secret_key = "123456"

CARPETA = "static/uploads"
app.config["UPLOAD_FOLDER"] = CARPETA

os.makedirs(CARPETA, exist_ok=True)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        correo = request.form["correo"]
        clave = request.form["clave"]

        if correo == "admin@gmail.com" and clave == "123456":

            session["correo"] = correo

            return redirect("/panel-admin")

        flash("Correo o contraseña incorrectos")

        return redirect("/login")

    return render_template("login.html")


@app.route("/panel-admin")
def panel_admin():

    if "correo" not in session:
        return redirect("/login")

    return render_template("panel_admin.html")


@app.route("/logout")
def logout():

    session.clear()

    flash("Sesión cerrada correctamente")

    return redirect("/login")


@app.route("/registrar-producto")
def registrar_producto():

    if "correo" not in session:
        return redirect("/login")

    return render_template("registrar_producto.html")


@app.route("/ver-productos")
def ver_productos():

    if "correo" not in session:
        return redirect("/login")

    return render_template("ver_productos.html")


# =========================
# FUNCIONES MYSQL (PAUSADAS)
# =========================

"""
@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    imagen = request.files["imagen"]

    nombre_imagen = ""

    if imagen and imagen.filename != "":
        nombre_imagen = secure_filename(imagen.filename)
        ruta = os.path.join(app.config["UPLOAD_FOLDER"], nombre_imagen)
        imagen.save(ruta)

    sql = '''
    INSERT INTO productos(nombre, precio, stock, imagen)
    VALUES(%s, %s, %s, %s)
    '''

    valores = (nombre, precio, stock, nombre_imagen)

    cursor.execute(sql, valores)
    conexion.commit()

    flash("Producto guardado correctamente")

    return redirect("/registrar-producto")


@app.route("/crear-admin")
def crear_admin():

    correo = "admin@gmail.com"
    clave = generate_password_hash("123456")
    rol = "Administrador"

    sql = '''
    INSERT INTO usuarios(correo, clave, rol)
    VALUES(%s, %s, %s)
    '''

    valores = (correo, clave, rol)

    cursor.execute(sql, valores)
    conexion.commit()

    return "Administrador creado correctamente"
"""


if __name__ == "__main__":
    app.run(debug=True)