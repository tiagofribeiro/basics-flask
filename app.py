from flask import Flask, request
from flask.globals import request
from flask.json import jsonify
from flask_restful import Resource, Api
from models import Atividades, Pessoas

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    # Busca os dados de uma pessoa a partir do nome
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id' : pessoa.id,
                'nome' : pessoa.nome,
                'idade' : pessoa.idade
            }
        except AttributeError:
            response = {
                'success' : False,
                'message' : 'Pessoa nao encontrada'
            }
        return response
    
    # Altera um dado da pessoa pesquisada
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados["nome"]
        if 'idade' in dados:
            pessoa.idade = dados["idade"]
        pessoa.save()
        try:
            response = {
                'id' : pessoa.id,
                'nome' : pessoa.nome,
                'idade' : pessoa.idade
            }
        except AttributeError:
            response = {
                'success' : False,
                'message' : 'Não foi possível realizar a alteração'
            }
        return response
    
    # Remove a pessoa pesquisada
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            pessoa.delete()
            mensagem = { 'success' : True, 'message' : f"{pessoa.nome} deletado(a) com sucesso." }
        except Exception:
            mensagem = { 'success' : False, 'message' : "Não foi possível remover este registro."}
        
        return mensagem

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [
            {
                'id' : i.id, 
                'nome' : i.nome, 
                'idade' : i.idade
            } 
            for i in pessoas
        ]
        return response

    def post(self):
        try:
            dados = request.json
            pessoa = Pessoas(nome=dados["nome"], idade=dados["idade"])
            pessoa.save()
            response = { 'success' : True, 'message' : f"{pessoa.nome} adicionado(a) com sucesso." }
        except Exception:
            response = { 'success' : False, 'message' : "Não foi possível adicionar esta pessoa." }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [
            {
                'id' : i.id, 
                'nome' : i.nome, 
                'pessoa' : i.pessoa.idade
            } 
            for i in atividades
        ]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados["pessoa"]).first()
        atividade = Atividades(nome=dados["nome"], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa' : atividade.pessoa.nome,
            'nome' : atividade.nome,
            'id' : atividade.id
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoas')
api.add_resource(ListaAtividades, '/atividades')

if __name__ == '__main__':
    app.run(debug=True)