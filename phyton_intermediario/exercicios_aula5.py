# Crie uma função para dizer se o numero é par ou impar.

def x (numero):
    multi_2 = numero % 2 == 0
    if multi_2:
        return f'{numero} este numero é par'
    return(f'{numero} este numero é impar')

print(x(2))
print(x(8))
print(x(5))