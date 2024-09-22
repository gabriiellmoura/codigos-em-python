"""
Closure e funções que retornam outras funções
Fechamento para resumir tudo. O que significa que eu posso resumir os codigos usando os 
recursos do phyton para retornar algo que eu quero, no caso def dentro de outro def 
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar # O phython precisa retornar algo, por esse motivo que estar aqui saudar, com parametro nome


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))