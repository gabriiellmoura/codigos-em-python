#IMC
nome = "José Gabriel"
altura = 1.60
peso = 59
imc = peso / (altura * altura) # altura ** 2 - outra forma de resolver
 
   #print (nome, 'tem', altura, 'de altura, pesa', peso, 'e seu imc é', imc)

'f-strings'
linha1 = f'{nome} tem {altura:.2f} de altura, pesa {peso:.2f} quilos e seu imc é {imc:.2f}'
print(linha1)
