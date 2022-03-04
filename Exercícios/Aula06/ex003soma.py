# algoritmo para ler dois números e mostrar a soma

n1 = int(input('Dígite um valor: '))
n2 = int(input('Dígite outro valor: '))
s = n1 + n2
print('A soma entre \033[1;33m{}\033[m e \033[1;33m{}\033[m é igual a \033[1;36m{}\033[m!'.format(n1, n2, s))