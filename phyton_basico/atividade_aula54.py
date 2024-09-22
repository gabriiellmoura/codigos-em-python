"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
valor1 = input('Digite um numero inteiro')
valor2 = int(valor1)
valor3 = valor2 / 2 # valor3 = valor2 % 0
valor_int = int(valor3)

if valor_int:
    print('O numero é par')
else:
    print('O numero é impar')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""