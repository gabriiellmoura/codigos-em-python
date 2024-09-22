'''
def soma(x, y):
   return  [x + y]

soma1 = soma(1, 3)
print(soma1)

soma2 = soma(5,5)
print(soma2)
'''


def soma(*args):
    total = 0
    for num in args:
        total = total + num
        print(total)


soma(1, 2, 3, 4, 5)