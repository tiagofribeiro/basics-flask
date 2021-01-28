from flask import Flask, json, request
from flask_restful import Resource, Api
from intermediary.habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"O desenvolvedor de ID {id} não existe."
            return {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API"
            return {"status": "erro", "mensagem": mensagem}
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": "sucesso", "mensagem": "Registro excluído!"}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        try:
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return {"status": "sucesso", "mensagem": "Desenvolvedor adicionado!"}
        except Exception:
            return {"status": "sucesso", "mensagem": "Erro ao adicionar desenvolvedor, verifique o valor das entradas."}

api.add_resource(Habilidades, '/habilidades')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Desenvolvedor, '/dev/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
