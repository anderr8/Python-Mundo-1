# Algoritmo para saber se o nome "Silva" está no nome ou no sobrenome de uma pessoa.

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

