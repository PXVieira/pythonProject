# criando um banco de dados
from peewee import *
from datetime import datetime
from time import sleep
from os import system as limpar
from mod_pack.database import *
from mod_pack.menu_cadastro import *
from mod_pack.numeros import *
from mod_pack.textos import *

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
        sleep(0.5)
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


class Cadastrar:
    def __init__(self, moto):
        self.moto = moto

    def moto():
        while True:
            moto = Strings.str_txt("Motorista: ")
            cpf = Strings.str_cpf("CPF: ")
            celular = Strings.str_cel("Celular: ")

            try:
                db_connect()
                cdt = Motorista.create(nome_moto=moto, cpf=cpf, n_celular=celular)
                print(f'"{moto}" Cadastrado com SUCESSO!')
                sleep(2)
                db_close()
                limpar("cls")
            except Exception as e:
                print(f'Erro! Não foi possível cadastrar. "{moto}"')

            sair = str(input("Continuar cadastrando? [S/N]: ")).upper().strip()[0]
            if sair == "S":
                pass
            elif sair == "N":
                break
            else:
                print("Erro! Opção inválida, apenas S ou N")


# db_connect()
# db_table()
# db_close()
