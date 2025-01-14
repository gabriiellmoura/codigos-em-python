"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) 
lista.pop() 
lista.append(60)
lista.append(70)

ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

lista = [10, 20, 30, 40]
lista.append('Luiz')

nome = lista.pop()
lista.append(1233)
del lista[-1]

# lista.clear()

lista.insert(100, 5)
print(lista[4])