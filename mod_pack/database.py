# criando um banco de dados
from peewee import *
from datetime import datetime
from time import sleep
from os import system as limpar

db = SqliteDatabase("base.db")


class Motorista(Model):
    nome_moto = CharField()
    cpf = CharField(unique=True)
    n_celular = CharField()

    class Meta:
        database = db


class Transportadora(Model):
    nome = ForeignKeyField(Motorista, backref="caminhao")
    transp = CharField()
    placa = CharField()
    modelo = CharField()

    class Meta:
        database = db


class Setor(Model):
    nome = ForeignKeyField(Motorista, backref="responsavel")
    nome_responsavel = CharField()
    setor = CharField()
    entrada = DateTimeField(default=datetime.now())
    saida = DateTimeField()

    class Meta:
        database = db


# criando e conectando banco de dados
def db_connect():
    try:
        db.connect()
        print("Conexão com o banco de dados realizada com SUCESSO!")
        sleep(2)
        limpar("cls")
    except Exception as e:
        print("Erro! Não foi possível realizar a conexão!\n", type(e), ":", e)


# criando as tabelas
def db_table():
    try:
        db.create_tables([Motorista, Transportadora, Setor])
        print("Tabelas do banco de dados criadas com SUCESSO!")
        sleep(2)
        limpar("cls")
    except Exception as e:
        print(
            "Erro! Não foi possível criar as tabelas do banco de dados!\n",
            type(e),
            ":",
            e,
        )


# fechando banco de dados
def db_close():
    try:
        db.close()
        print("Banco de dados encerrado com SUCESSO!")
        sleep(2)
        limpar("cls")
    except Exception as e:
        print("Erro! Não foi possível encerrar banco de dados!\n", type(e), ":", e)


# db_connect()
# db_table()
# db_close()
