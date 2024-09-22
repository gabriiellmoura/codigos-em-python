def decorador (a=None, b=None, c=None):
    def funcao(func):
        print('decoraodor 1')

        def aninhada (*args, **kwargs):
            #print('paramentros decorador, ', a, b, c)
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return funcao

@decorador(1, 2, 3)
def soma(x, y):
    return x + y

soma1 = soma(10, 5)
print(soma1)