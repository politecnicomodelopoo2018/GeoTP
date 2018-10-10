from flask import *
from pymongo import *
from classCamping import *




client = MongoClient('localhost', 27017)
db = client.GeoTP
campings = db.campings




olcampings = Camping.getListaFromMongo(campings)


print(olcampings[0].id)




app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def Index():
    return redirect("/paginaPrincipal")

@app.route('/paginaPrincipal')
def paginaPrincipal():
    return render_template("paginaPrincipal.html", listaCampings=Camping.getListaFromMongo(campings))

@app.route('/camping')
def CampingPage():
    return render_template("camping.html", camping=Camping.getCamping(campings, int(request.args.get("campingId"))))

@app.route('/allCampings')
def allCampings():
    return render_template("allCampings.html", listaCampings=Camping.getListaFromMongo(campings))




if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
    app.run(debug=True) # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal