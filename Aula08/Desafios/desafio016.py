# criar um algoritmo quer leia um número Real e mostre a parte inteira

from math import ceil
num = float(input('Dígite um número: '))
inteira = int(num)
print('O número {} e a parte inteira é {}'.format(num, ceil(inteira)))