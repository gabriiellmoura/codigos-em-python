# 123. (Parte 2) Métodos úteis nos dicionários Python (dict)
p1 = {
    'n1' : 'Gabriel',
    'n2' : 'Moura'
}

#print(p1['n2'])
print(p1.get('n1', 'Infelizmente o valor não existe'))

#pop -> Remove um item do seu dicionario mas salvando o valor que estar nela.
# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)
