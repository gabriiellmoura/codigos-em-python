'''
Sintaxe em python e boas praticas de programação

CONSTANTES -> Dados que não mudam com o fluxo do programa.
Dentro do python não existem CONSTANTES, o tem é um concenso que diz que dados
que não vareiam devem ser escritos em maiusculo.

Boas praticas
> Evitar usar muitos IF
        <- Quanto mais complexos, mais blocos dentro de blocos, o codigo fica mais dificil é 
para outras pessoas entenderem o que atraplha no dia a dia do programador. 
'''
velocidade_atual = 70
local_atual = 100


RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade_atual > RADAR_1:
    print('Você ultrapassou o limite maximo de velocidade permitida')

if local_atual >= (LOCAL_1 + RADAR_RANGE) \
        and local_atual >= (LOCAL_1 - RADAR_RANGE):
          velocidade_atual > RADAR_1
print('Carro multado em radar 1')