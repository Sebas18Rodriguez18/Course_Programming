#En este se mostrará el funcionamiento del metodo index en una lista.

list_number = [1,2,3,4,5,6,7,8,9,0]
              #Creamos una lista con valores númericos enteros.
print (list_number)
print ()
print("*************************************************************")
print ()
x = list_number.index(7)
              #Con el metodo index lo que hacemos es mirar en que posición 
              #de la lista se encunetra el valor deseado.
print (x)
              #En este momento la posición del valor de nuestra lista "7" 
              #esta en la posición 6 debido a que se empieza a contar desde el 0.