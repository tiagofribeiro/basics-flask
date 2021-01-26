from flask import Flask, jsonify, json, request

app = Flask(__name__)

# GET básico
@app.route("/<int:id>")
def pessoa(id):
    return {'id': id, 'nome': 'Tiago', 'profissao':'Dev'}

# GET com mútiplos parâmetros
@app.route('/soma/<int:valor1>/<int:valor2>')
def soma(valor1, valor2):
    return {'soma':valor1 + valor2}

# POST - body
@app.route('/somaPost', methods=['POST'])
def somaPost():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return {'soma': total}

# Múltiplos métodos
@app.route('/somaMult', methods=['POST', 'GET'])
def somaMult():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    else:
        total = 2 + 2
    return {'soma': total}


if __name__ == '__main__':
    app.run(debug=True)