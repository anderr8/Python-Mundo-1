# Programa para calcular o Sálario de um funcionário e dar um aumento de 15% para quem recebe até R$1250,00, e 10% de aumento para quem recebe mais que R$1250,00.

salário = float(input('Qual é o sálario do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quam ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))