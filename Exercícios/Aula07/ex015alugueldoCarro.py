# Algoritmo para calcular os km rodados por dias de um carro alugado e, calcular o preço a ser pago, sabendo que o valor custa R$60 por dia e R$0,15 por km

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))