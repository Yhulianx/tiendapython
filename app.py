from flask import Flask, render_template, request, redirect, flash, session
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
# GUARDADO TEMPORAL
# =========================

@app.route("/guardar", methods=["POST"])
def guardar():

    if "correo" not in session:
        return redirect("/login")

    nombre = request.form["nombre"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    print("Producto:")
    print(nombre)
    print(precio)
    print(stock)

    flash("Producto registrado correctamente")

    return redirect("/registrar-producto")


if __name__ == "__main__":
    app.run(debug=True)