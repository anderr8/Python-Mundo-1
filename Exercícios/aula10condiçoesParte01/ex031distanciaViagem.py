# Algoritmo para calcular distancia em Km de um viagem, viagens de até 200Km o valor é de R$0,50, acime de 200Km o valor é de R$0,45

distância = float(input('Qual é a distãncia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
'''Exemplo uma forma simplificacda:
preço = distância * 0.50 if distância <= 200 else distância * 0.45'''

print('E o preço da sua passagem será de R${:.2f}.'.format(preço))