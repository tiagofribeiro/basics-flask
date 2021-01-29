from models import Pessoas, Usuarios

# ================= Pessoas =================

# Realiza um insert na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='alex', idade=999)
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

# ================= Usuários =================

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    print(usuario)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print=(usuarios)


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()
    insere_usuario("teste", "senha")
    consulta_usuarios()