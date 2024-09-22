"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1 #Essa é a estrutura que segura o contador e mantem o codigo livre de laços infinitos.

    if contador == 6: #Nesse exemplo o professor utilizou os if's para mostrar o CONTINUE
        continue

    if contador >= 10 and contador <= 27:
        continue #usamos quando queremos pular algo dentro do programa, ainda não sei quando e como usar direito

    print(contador)

    if contador == 40:
        break # O break ele para o laço independente da logica aplicada, sempre que aparece o codigo é forçado a parar


print('Acabou')