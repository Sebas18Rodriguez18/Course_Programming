#En este se mostrará el funcionamiento del metodo extend en una lista.

list_number = [1,5,2,3,4,5,6,7,8,9,0,5]
              #Creamos una lista con valores númericos enteros.
list_fruits = ["apple","pear","melon","watermelon","banana","coco"]
              #Creamos una otra lista con valores String.
print (list_number)
print ()
print (list_fruits)
print("*************************************************************")
print ()
list_number.extend(list_fruits)
              #Con el metodo extend lo que hacemos es agregarle valores de una lista a la otra.
print (list_number)