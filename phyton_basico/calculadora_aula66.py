while True:
    numero1 = input('Digite um numero ')
    numero2 = input('Digite um outro numero ')
    ope = input('Digite a operação ')
    num1_float = 0
    num1_float = 0
    
    
    
    num_val = None
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        num_val = True
    except:
        num_val = None

    if num_val is None:
        print('numeros incorretos digite novamente')
        continue
    ope_permitidos = '+-/*'

    if ope not in ope_permitidos:
        print('O operador que voce digitou não é valido')
        continue
    if len(ope) > 1:
        print ('Digite apenas um operador')
        continue
    
    
    if ope == '+':
        print(num1_float + num2_float)
    elif ope == '-':
        print(num1_float - num2_float)
    elif ope == '/':
        print(num1_float / num2_float)
    elif ope == '*':
        print(num1_float * num2_float)
    else:
        print('Esse codigo não deveria chegar aqui')
    
    sair = input('Você quer sair?[s]im ' ).lower().startswith('s')

    if sair is True:
        break