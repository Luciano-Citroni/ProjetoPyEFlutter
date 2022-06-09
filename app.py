from crypt import methods
import requests
import os
from flask import Flask
from flask import request
from Scripts import Consultas, cadastrar


app = Flask(__name__)


@app.route("/<ra>", methods=['GET'])
def consultarRa(ra):
    return Consultas.consultarRa(ra)
    # if ConsultarRA.consultarRa(ra) == True:
    #     return "Encontrou"
    # else:
    #     return "Nada foi encontrado"

@app.route("/All", methods=['GET'])
def consultarTodos():
    return Consultas.consultarTodos()

@app.route("/Cadastrar", methods=['GET', 'POST'])
def cadastro():
    ra = request.args.get("RA")
    return ra



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)