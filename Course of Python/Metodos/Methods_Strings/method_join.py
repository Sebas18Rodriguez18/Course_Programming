import os
os.system('cls')

'''
Empezaremos el metodo de cadenas llamado 'join' que funciona asi.
El metodo join sirve para pasar de una lista a una cadena de texto, y se ve algo así:
'''

words = ['hola', 'mundo', 'hola', 'python']
print (words)
print()
print('*****************************************************************************************')
print()
print(' '.join(words))
                            #Se coloca el ' '.join(variable) para la separación de las palabras,
                            #se puede utilizar todo tipo de iteración
print()
print('-'.join(words))
print()
print('.'.join(words))
print()
print('+'.join(words))
print()
print(';'.join(words))
print()