'''
Métodos úteis dos dicionários em Python
 len - quantas chaves || print(len(pessoa))
 keys - iterável com as chaves
 values - iterável com os valores
 items - iterável com chaves e valores
 setdefault - adiciona valor se a chave não existe
 copy - retorna uma cópia rasa (shallow copy)
 get - obtém uma chave
 pop - Apaga um item com a chave especificada (del)
 popitem - Apaga o último item adicionado
 update - Atualiza um dicionário com outro
'''
# Quando se usa a mesma chave, ou seja, quando se atribui algo para um parametro dentro das funcoes
# não se cria novos valores eles apenas atualizam e apontam para o ultimo valor referenciado.

x = input('digite seu nome')
y = input('agora o seu sobrenome')

dados_pessoa = {
    'nome': x,
    'sobrenome': y
}
for chave, valor in dados_pessoa.items():
    print(chave, valor)