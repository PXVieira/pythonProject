from tqdm import tqdm
from time import sleep

from mod_pack.database import *
from mod_pack.menu_cadastro import *
from mod_pack.numeros import *
from mod_pack.textos import *


# menu principal, cadastros e edição
def menu():
    menu = [
        "Cadastrar motorista",  # 1
        "Cadastrar transportadora",  # 2
        "registrar entrada",  # 3
        "Registrar saída",  # 4
        "Exibir registros",  # 5
        "Sair",  # 6
    ]

    Separadores.titulo("MENU PRINCIPAL")

    for i, v in enumerate(menu):
        print(f"{i + 1} -→ {Cor.azul(v)}")

    Separadores.linha()


def esc(e):
    sair = True
    while sair:
        if e == 1:
            Cadastrar.moto()
        if e == 2:
            ...
        if e == 3:
            ...
        if e == 4:
            ...
        if e == 5:
            ...
        else:
            sair = False
            for i in tqdm(range(3), desc="Salvando os dados..."):
                sleep(0.4)
            break
