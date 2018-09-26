from flask import *

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def Index():
    return redirect("/paginaPrincipal")

@app.route('/paginaPrincipal')
def paginaPrincipal():
    return render_template("paginaPrincipal.html")

@app.route('/camping')
def Camping():
    return render_template("camping.html")




if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
    app.run(debug=True) # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal