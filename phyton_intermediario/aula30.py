from itertools import groupby


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
'''
#alunos = ['a', 'a', 'a', 'b', 'c', 'd']
grupos = groupby(alunos)

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
'''
def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key= ordena)
grupos = groupby(alunos_agrupados, key= ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)