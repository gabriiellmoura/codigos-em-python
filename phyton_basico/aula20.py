'''
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista_A = lista1 + lista2
print(lista_A)
'''
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[4] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


# For in com listas - Aula 85
lista_nova = ['Gabriel', 'João', 'Maria']

for nome in lista_nova:
    print(nome)
