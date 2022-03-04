# algoritmo para calcular média

n1 = float(input('Dígite a primeira nota: '))
n2 = float(input('Dígite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
   #print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')