#Calculando desconto

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))


# fórmula :  R$10,00   100%
#                 x      5%

#multiplica -> R$10,00 por 5% = o valor corresponde ao  X
#dividi     -> x  por 100%