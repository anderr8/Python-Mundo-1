#Conversor de moedas

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.27
euro = real / 6.17
libra = real / 6.88
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, libra))