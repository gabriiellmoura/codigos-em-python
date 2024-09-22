#try finally
'''
Essa é a condição onde o FINALLY ele vai ser executado de qualquer forma, independete do erro
que ocorra.
'''
try:
    print('abrir o arquivo')

except ZeroDivisionError:
    print('dividiu por zero')
finally:
    print('fechar o arquivo')

