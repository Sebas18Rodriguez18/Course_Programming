import os

os.system('cls')

#En este se mostrará el funcionamiento del metodo sort en una lista.

list_number = [4,8,2,0,7,1,5,9,3,6]
              #Creamos una lista con valores númericos enteros.
print (list_number)
print ("↑ Lista original")
print ()
print ()

list_number.sort()
            #Con el metodo sort lo que hacemos es ordenar la lista. 
print (list_number)
print ("↑ Lista ordenada")
print()
print()

'''
Para el metodo sort hay dos parámetros opcionales para usar llamados "reverse" y "key"
estos parámetros sirven de la siguiente manera.

Empezaremos con el parametro reverse.
Este comúnmente sirve para ordenar la lista en orden descendente y se usa así:
'''

list_number.sort(reverse=True)
print (list_number)                 #En otras palabras la lista ira de mayor a menor.
print ("↑ Lista ordenada de forma descendente")          #Este también sirve para Strings
print()
print("*************************************************************")
print()
list_fruits = ["apple","pear","melon","watermelon","banana","coco"]
              #Creamos una otra lista con valores String.
print(list_fruits)
print ("↑ Lista original")
                            #En otras palabras la lista ira en orden alafabético de atras hacia 
list_fruits.sort()                          # #adelante osea de la Z - A.
print()
print(list_fruits)
list_fruits.sort(reverse=True)
print ("↑ Lista ordenada de forma ascendente A-Z")
print()
print(list_fruits)
list_fruits.sort(reverse=False)
print ("↑ Lista ordenada de forma descendente Z-A")
print()
                            #Tanto para valores int, float o String el metodo sort con el parámetro
                            #reverse puedes camniar el "True" por un "False"
                            #y este hará lo contrario.
print()
print("*************************************************************")
print()
#Ahora vamos con el parámetro  key del método sort.
#Este comúnmente sirve para especificar el orden de los criterios y se usa así:

list_fruits = ["apple","pear","melon","watermelon","banana","coco"]
              #Creamos una otra lista con valores String.
print(list_fruits)
print ("↑ Lista original")
              #En este caso ordenaremos la lista de frutas por orden de carácteres de menor a mayor.
def myFruits(f):
  return len(f)
list_fruits.sort(key=myFruits)
print()             #Este función lo que hizo fue que tomara como argumento "f" representando los valores uno por uno de la lista
print(list_fruits)  #Y de esta manera pudiese ver la longitud mediante len() y así poderlos ordenar por su tamaño de caracteres.
print ("↑ Lista ordenada de según el tamaño de caracteres")

print()
print("*************************************************************")