from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcetagem):
    return round(valor * porcetagem, 2)

aumentarDezPorcento = partial(
    aumentar_porcentagem,
    porcetagem= 1.1
)
'''
novos_produtos = [
     {**p, 'preco': aumentarDezPorcento(p['preco'])}
    for p in produtos
]
'''
def muda_precos(produto):
    return {
        **produto, 'preco': aumentarDezPorcento(produto['preco'])
    }

novos_produtos = list(map(
    muda_precos,
    produtos
))

print_iter(produtos)
print_iter(novos_produtos)