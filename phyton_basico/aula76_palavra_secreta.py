"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_sec = 'gato'
cont = 0
letras_acert = ''

while True:
    letra_dig = input('digite uma letra: ')
    cont += 1
    
    if len(letra_dig) > 1:
        print('digite apenas uma letra')
        continue
    
    if letra_dig in palavra_sec:
        letras_acert += letra_dig
    
    for letra_sec in palavra_sec:
        if letra_sec in letras_acert:
            print(letra_sec)
        else:
            print('*')
