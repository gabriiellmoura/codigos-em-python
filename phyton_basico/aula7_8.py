# Metodos são funções que podem ser atribuidas aos dados dos objetos em python
# Paramentro nomeado é quando eu atribuo um nome para os argumentos.
# Ex: nome3=C / nome3 é o paramentro e C é o argumento.
# Quando uma função esta dentro de um objeto nos chamamos de METODO.

# Aula 8 - Usando o input para coletar dados dos usuarios
nome =  input('qual seu nome?')
print(f'o seu nome é {nome}')

num_1 = input('digite um numero: ')
num_2 = input('digite outro numero: ')

int_num1 = int(num_1)
int_num2 = int(num_2)

soma = int_num1 + int_num2

print(f'A soma dos dois numeros é {soma}')