from flask import Flask, render_template
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route("/")
def index():
    return "Hola Mundo! CodigoFacilito"


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("errores/404.html"), 404
