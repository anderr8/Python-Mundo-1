n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
su = n1 - n2
print('A soma é {}, produto é {} e a divisão {:.2f}.'.format(s, m, d), end='>>>')#exemplo -> end='' => continua na mesma linha
print('Divisão inteira é {}, a potencia é {:.2f} e a divisão {:.2f}'.format(di, e, su))
#print('A soma vale {:w^20}.'.format(n1+n2)) exemplo