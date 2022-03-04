# algoritmo para mostrar de um produto à vista ou parcelado.

pagamento = float(input('Qual o valor deste produto?'))
àvista = pagamento - (pagamento * 60 / 100)
print('O pagamento à vista saí por R${:.2f} com desconto de 60%.'.format(àvista))
parcelado = pagamento + (pagamento * 1 / 100)
print('O pagamento parcelado saí por R${:.2f} com 1% de acréscimo.'.format(parcelado))