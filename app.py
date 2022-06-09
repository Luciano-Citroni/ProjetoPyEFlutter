import requests
from flask import Flask
import json
from Scripts import ConsultarRA

app = Flask(__name__)

@app.route('/')
def ConsultarRa():
    return 'Olá mundo'

#app.run()

if __name__ == '__main__':
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()