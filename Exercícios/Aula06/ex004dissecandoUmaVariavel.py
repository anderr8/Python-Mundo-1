# Algoritmo par mostrar um o que foi dígitado e mostrar se é tipo primitivo e todas as informações possíveis.

a = input('Dígite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalnum())
print('É alfanumerico? ', a.isalpha())
print('Está em maíusculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está captalizada? ', a.istitle())