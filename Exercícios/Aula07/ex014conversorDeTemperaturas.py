# Algoritmo para converter °Celsius em fahrenheit

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32 # não a necessidade de usar parênteses, proque entra na regra de precedência
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))