# Algoritmo para ler um salário e mostrar o valor do novo salário com 15% de aumento.

salário = float(input('Qual o novo salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))