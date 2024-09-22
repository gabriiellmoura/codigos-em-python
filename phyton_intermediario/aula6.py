"""
Higher Order Functions
Funções de primeira classe
"""

'''
def saudacao_aula(msg):
    return msg


saudacao_aula_2 = saudacao_aula

v = (saudacao_aula('Bom dia'))
print(v)
'''


'''

v = input('digite o seu nome')

def saudacao(v):
    return v

print(saudacao(v))
'''


def saudacao_aula(msg):
    return msg

#print(saudacao_aula('Bom dia'))


def executa(funcao, msg):
    return funcao(msg)

#saudacao_aula_2 = saudacao_aula

v = executa(saudacao_aula, 'bom dia') #v = executa(saudacao_aula_2)
print(v)

# Script da aula
'''
def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)
'''