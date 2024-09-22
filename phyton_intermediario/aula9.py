pessoa = {}

chave = 'nome_completo'
pessoa[chave] = 'José Gabriel'
pessoa['sobrenome'] = 'Moura'

#del pessoa['sobrenome']

print(pessoa[chave])


if pessoa.get ('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])