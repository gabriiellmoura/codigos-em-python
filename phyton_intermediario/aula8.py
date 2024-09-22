"""
Dicionários em Python (tipo dict)
 Dicionários são estruturas de dados do tipo
 par de "chave" e "valor".
 Chaves podem ser consideradas como o "índice"
 que vimos na lista e podem ser de tipos imutáveis
 como: str, int, float, bool, tuple, etc.
 O valor pode ser de qualquer tipo, incluindo outro
 dicionário.
 Usamos as chaves - {} - ou a classe dict para criar
 dicionários.
 Imutáveis: str, int, float, bool, tuple
 Mutável: dict, list
"""
'''
 Esse tipo de dado, ou estrutura, podemos usar para acessar algo realizado sem ter que ficar 
 reescrevendo codigo toda hora. A mesma logica das tuplas, escreve o codigo e armazena na memoria
 com variaveis.
'''

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

for chave in pessoa:
    print(chave, pessoa[chave])
#print(pessoa['idade'])