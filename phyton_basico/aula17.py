# Aula 72. Introdução ao for / in - estrutura de repetição para coisas FINITAS

# O while ele é usado quando não sabemos quantas repetições precisaremeos ter, o que o torna 
# imprevissivel. Quando conseguimos prever quantas ações o usuario ele vai toamar utilizamos
# outras formas de montar o codigo para atingir determinados resultados que queremos.
# ->       Essa é a diferença para que usar laços FINITOS ou INFINITOS

# Codigo para senha de usuario
senha_salva = '1234'
senha_for = ''
repeticoes = 0

while senha_salva != senha_for:
    senha_for = input(f'sua senha ({repeticoes}x): ')
    repeticoes += 1
print('voce entrou')
    
   

'''
num1 = range(10)     -> O step usamos para "ir" ou "voltar" dentro da variavel.
for num2 in num1:
    print(num2)
'''