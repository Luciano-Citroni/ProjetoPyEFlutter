import requests
import os
from flask import Flask
from Scripts import ConsultarRA


app = Flask(__name__)


@app.route("/")
def index():
    ra = 112
    if ConsultarRA.consultarRa(ra) == True:
        return "Encontrou"
    else:
        return "Nada foi encontrado"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)