import os
os.system('cls')

'''
Empezaremos el metodo de cadenas llamado 'strip' que funciona asi.

El metodo strip sirve para limpiar el texto de espacios u otras cosas
(cabe recalcar que el método strip no sirve para en medio de la cadena de texto solo sirve para el inicio y el fin)
y se ve algo así:
'''

words = '   Hola Mundo   '
words2 = '***Hola Mundo***'
words3 = '___Hola Mund____'
print (words)
print (words2)
print (words3)
print()
print('*****************************************************************************************')
print()
print(words.strip())
print ('↑ Texto limpio')
print()
print(words2.strip('*'))
print ('↑ Texto limpio de los (*)')
print()
print(words3.strip('_'))
print ('↑ Texto limpio limpio de los ( _ )')
print()