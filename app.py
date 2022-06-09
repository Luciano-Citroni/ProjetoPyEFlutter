from crypt import methods
import requests
import os
from flask import Flask
from flask import request, jsonify
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

@app.route("/Cadastrar", methods=['POST'])
def cadastro():
    data = request.json
    return jsonify(data)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)