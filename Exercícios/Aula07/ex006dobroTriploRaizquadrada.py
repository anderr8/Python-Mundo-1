# Algoritmo para calcular o dobro, triplo e a raíz quadrada

#n = int(input('Dígite um número: '))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('O dobro de {} vale {}.'.format(n, d))
#print('O triplo de {} vale {}. \nA raíz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

# Exemplo:
n = int(input('Dígite um número: '))
print('O dobro de {} vale {}.'.format(n,(n*2)))
print('O triplo {} vale {}. \nA raíz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))
                                                                #exemplo raiz quadrada:n, (n**(1/2))