from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column, ForeignKey

# Criação das propriedades do banco e da sessão
engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Facilita a criação de queries para a manipulação através das classes
Base = declarative_base()
Base.query = db_session.query_property()

# Criação da tabela pessoas
class Pessoas(Base):
    __tablename__ = "pessoas"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # Retorna o resultado da consulta
    def __repr__ (self):
        return f'<Pessoa {self.nome}>'
    
    # Realiza o commit de alguma operação
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Deleta um registro e realiza o commit
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Criação da tabela atividades
class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

# Cria o banco e a sessãos
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()