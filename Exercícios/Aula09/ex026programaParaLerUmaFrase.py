# algoritmo para ler uma frase, mostrar quantas letras "A" tem, qual a posição ela está.

frase = str(input('Dígite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))