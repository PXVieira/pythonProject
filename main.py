#  mods externos
from peewee import *
from tqdm import tqdm

# mods locais
from mod_pack.database import *
from mod_pack.menu_cadastro import *
from mod_pack.numeros import *
from mod_pack.textos import *

menu()
e = Numbers.n_int_range("Sua escolha: ", f=6)
esc(e)
