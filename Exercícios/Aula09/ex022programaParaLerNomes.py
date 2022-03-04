# Algoritimo para ler o nome de um pessoa e analisar o nome digitado

nome = str(input('Dígite o seu nome: ')).strip() # strip => elimina os espaços vázios a direita e a esquerda
print('analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.\n'.format(nome.find(' ')))

# Outro exemplo
print('Separar nome e sobrenome:')
separar = nome.split()
print(separar)
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separar[0], len(separar[0]))) # zero é o local que está o primeiro nome