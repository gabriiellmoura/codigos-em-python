pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Moura',
}
#for chave, valor in pessoa.items():
#    print(chave, valor)

dados_pessoa = {
    'idade': 22,
    'altura': 1.6,
}
dados_completos = {**pessoa, **dados_pessoa}

def argumentos(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
#argumentos(nome='joana', qlq=123)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
argumentos(**configuracoes)
print(__name__)