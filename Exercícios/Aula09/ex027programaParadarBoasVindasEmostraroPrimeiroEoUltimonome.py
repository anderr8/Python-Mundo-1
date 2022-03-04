# Algoritmo para dar Boas Vindas e mostrar o primeiro e o último nome.

n = str(input('Dígite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Tudo bem com você?')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
print('-'*20)
print('Sim!, estou muito bem!')
