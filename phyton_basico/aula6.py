# Operadores aritimeticos
"""
Os operadoradores aritimeticos dentro do python sao os mesmo que usamos na
matematica, e a forma como utilizamos esses operadores muda pouca coisa.
"""
soma = 5 + 5
print('soma', soma)

multiplicacao = 2 * 2
print ('multiplicacao', multiplicacao)

divisao = 10 / 3
print ('divisao', divisao)

divisao_int = 10 // 5
print ('divisao inteira', divisao_int)

exponeciacao = 12 ** 3 # doze elevado a tres.
print ('exponenciacao', exponeciacao)

modulo = 23 % 3
print ('modulo', modulo)
# Resto da divisao.

# Concatenação e repetição
"""
Podemos usar o '+' para juntar o que queremos e exibir na tela.
"""
concatenacao = 'José' + ' ' + 'Gabriel'
print(concatenacao)

a_dez_vezes = 'A' * 10
jose_trez_vezes = 'José' * 3
print(a_dez_vezes)
print(jose_trez_vezes)

# Precedencia, ordem
'''
1. (n + n)
2. **
3. * / // %
4. + e -
'''
# Lembrando que os parenteses eles são resolvidos o mais internos primeiro,
# ou seja de dentro para fora.