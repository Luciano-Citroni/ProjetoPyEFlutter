import requests
link = 'https://flutterepy-default-rtdb.firebaseio.com/'

def consultarRa(vRa):
    consultar = requests.get(f'{link}/Alunos/.json')
    resultadoConsulta = consultar.json()
    for idAluno in resultadoConsulta:
        raResultado = resultadoConsulta[idAluno]['RA']
        if vRa == raResultado:
            return resultadoConsulta[idAluno]


def consultarTodos():
    consultar = requests.get(f'{link}/Alunos/.json')
    resultadoConsulta = consultar.json()
    return resultadoConsulta