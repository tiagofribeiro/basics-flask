from models import Pessoas

# Realiza um insert na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Roberto', idade=26)
    print(pessoa)
    pessoa.save()

# Realiza um select na tabela pessoas
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)

# Realiza um update na tabela pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Tiago").first()
    pessoa.idade = 23
    pessoa.save()

# Exclui um registro na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Roberto").first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()