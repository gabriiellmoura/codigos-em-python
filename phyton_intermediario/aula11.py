# 122. Shallow Copy vs Deep Copy em dados mutáveis Python

#   Usar o sinal de atribuição não siginifica que voce vai estar copiando os valores, somente apontando 
# para algo na memoria e atualizando os valores. Cuidado com isso pois pode da problema com dados mutaveis.
#   Resumindo, o metodo copy não faz uma copia dos dados gravados, apenas linka em uma variavel e entrega
# um valor igual. para cortornar isso ultizamos uma 'façanha' que é importar a biblioteca copy e usar o deepcopy
# que faz uma copia mais profunda em subniveis dos dados. Isso ocorre por conta de processamento pois se estieverem
# em muitos dados algumas maquinas podem não suportar devido ao tamanho dos arquivos.

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)