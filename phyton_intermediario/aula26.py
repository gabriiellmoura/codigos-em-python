'''
def fora(x):
    a = x
    def dentro():
        return a # A variavel "a" é considerada livre pois não esta definida no escopo da função "dentro" 
    return dentro

y = fora(10)
z = fora(20)
print(y())
print(z())
'''
def concatenar(string_inicial):
    final = string_inicial
    def interna(valor_concatenar=''):
        nonlocal final # Impede que erros ocorram buscando os valores na função concatenar.
        final += valor_concatenar
        return final
    return interna
a = concatenar('a')
print(a('b'))
print(a('c'))
print(a('d'))
