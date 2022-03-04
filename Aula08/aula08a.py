# Importação de bibliotecas
# ceil => arredonda para cima
# floor => arredonda para baixo
# trunc => para truncar um número
# pow => para potência
# sqrt => para raíz quadrada
# factorial => para fatorar um número

#*import math
#num = int(input('Dígite um número: '))
#raíz = math.sqrt(num)
#print('A raíz de {} é igual a {:.2f}'.format(num, raíz))

from math import sqrt, floor
num = int(input('Dígite um número: '))
raíz = sqrt(num)
print('A raíz de {} é igual a {}'.format(num, floor(raíz)))