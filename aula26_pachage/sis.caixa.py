valor = input('digite o valor')
qtidade = input('Digite a quantidade')
x = float(valor)
y = int(qtidade)
total = x * y

print(f'Valor final da compra {total:.2f}')

recebido = input('Digite agora a quantia paga')
z = float(recebido)
print('Quantia recebida', z)
a = z - total

troco = '{:,.2f}'.format(a)
print('Seu troco', troco)