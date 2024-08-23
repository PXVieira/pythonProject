from mod_pack.textos import *

# menu principal, cadastros e edição
menu = [
    "Cadastrar motorista",
    "Cadastrar transportadora",
    "registrar entrada",
    "Registrar saída",
    "Exibir registros",
    "Sair",
]

for i, v in enumerate(menu):
    print(f"{i + 1} -→ {Cor.azul(v)}")
