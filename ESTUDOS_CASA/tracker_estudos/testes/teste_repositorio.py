import sys
import os


caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, caminho_raiz)


from materia import Materia
from sessao import Sessao
from repositorio import Repositorio

from repositorio import Repositorio
from materia import Materia
from datetime import date
from sessao import Sessao



repo = Repositorio("teste.db")


materia_python = Materia("Python", 120) 
repo.salvar_materia(materia_python)

data_estudo = date(2026, 7, 20)
sessao_python = Sessao(materia_python, 60, data_estudo) 
repo.salvar_sessao(sessao_python)


materias = repo.listar_materias()
sessoes = repo.listar_sessoes()


for mat in materias:
   
    print(mat.nome, mat.meta_semanal) 

for sessao in sessoes:

    print(sessao.materia.nome, sessao.minutos, sessao.data)