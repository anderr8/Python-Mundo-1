frase = 'Curso em Vídeo Python' # string é imutável =. é díficil de mudar
print(frase[0])
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])