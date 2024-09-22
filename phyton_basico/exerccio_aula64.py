'''
nome = 'jose gabriel'
nome_acess = len(nome)
nome[0]

while nome_acess == nome:
    print(nome, '*')
    break
'''
nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)