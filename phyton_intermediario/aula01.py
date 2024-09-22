"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

"""
 def Print(a, b, c): -> Paramentros. Ou seja, algo especifico que eu quero colocar aqui e 
 atribuir valores posteriormente. Esses valores são chamados de argumentos.
     print('Várias1')
     print('Várias2') 
     print('Várias3')
     print('Várias4')

 def imprimir(a, b, c):
     print(a, b, c) -> Argumentos.


 imprimir(1, 2, 3)
 imprimir(4, 5, 6)

Resumindo, o parametro se usa na definição da função e os argumentos são os
valores em si.

Argumentos posicionais são aqueles onde a ordem altera o resultado do codigo.
Argumentos nomeados são aqueles que possuem uma palavra chave para serem executados.
  ->Nota: soma(1, y=2, z=5). Logo após nomear um argemento todos os outros logo após precisam ser nomeados tambem.

"""

"""
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

"""
ent = input('Digite o seu nome')
def imprimir(usuario):
    print(f'Olá, {usuario}!')

imprimir(ent)

"""
def soma(x, y, z): -> Definição de função
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma -> Nome da função.
soma(1, 2, 3) -> Execução de função.
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')

"""