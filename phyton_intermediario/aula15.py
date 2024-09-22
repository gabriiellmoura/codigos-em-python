# Empacotamento e desempacotamento de dicionarios
#a, b = 1, 2
#print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Sousa',
}
'''
a, b = pessoa.values() #itens()
print (a, b)
'''
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
dadosCompletos = {**pessoa, **dados_pessoa}

print(dadosCompletos.values())