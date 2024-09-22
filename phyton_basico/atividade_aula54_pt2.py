"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('informe a hora')
hora_int = int(hora_str)

if hora_int >= 0 and hora_int <= 11:
    print('bom dia')

elif hora_int >= 12 and hora_int <= 17:
    print('boa tarde')

elif hora_int >= 18 and hora_int <= 23:
    print('boa noite')
else:
    print('Por favor digite uma hora valida')
