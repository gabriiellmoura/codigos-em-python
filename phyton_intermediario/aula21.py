iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #iterable.__iter__()
#print(next(iterator))
'''
O problema dos dados muito grandes é que podem deixar o arquivo pesado 
pode ser um problema. Pensando nisso existem metodos e recursos para que possamos
salvar os dados de uma forma mais leve e acessalos usando iterador e generator.
'''
generetor = (n for n in range(10)) #[n for n in range(10)]
print(generetor)
'''
Iteretor: meche com iteravel, é uma classe que meche com iter e next
Generetor: função que para
'''

'''
def gentor (n=0):
    yield 1
    print('continuando...')

    yield 2
    print('mais uma vez')

    yield 3
    print('vou terminar')
    return('ACABOU')

gen = gentor(n=0)
for n in gen:
    print(n)
'''
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return


gen = generator(maximum=10)
for n in gen:
    print(n)
