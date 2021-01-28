from flask import Flask, request, json, jsonify

app = Flask(__name__)

# Lista pré-populada com 2 desenvolvedores
desenvolvedores = [
    {
        "id" : 0,
        "nome" : "Tiago",
        "habilidades" : ["Python", "React", ".NET"]
    },
    {
        "id" : 1,
        "nome" : "Roberto",
        "habilidades" : ["Python", "Angular", ".NET"]
    }
]

# Busca, edita e deleta um desenvolvedor a partir do seu ID (index)
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"O desenvolvedor de ID {id} não existe."
            return {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API"
            return {"status": "erro", "mensagem": mensagem}
        return response
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return {"status": "sucesso", "mensagem": "Registro excluído!"}

# Lista todos os desenvolvedores e cria um novo
@app.route('/dev', methods=['GET', 'POST'])
def lista_dev():
    if request.method == 'POST':
        try:
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return {"status": "sucesso", "mensagem": "Desenvolvedor adicionado!"}
        except Exception:
            return {"status": "sucesso", "mensagem": "Erro ao adicionar desenvolvedor, verifique o valor das entradas."}
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run(debug=True)