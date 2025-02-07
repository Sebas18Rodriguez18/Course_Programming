#En este se mostrará el funcionamiento del metodo count en una lista.

list_number = [1,5,2,3,4,5,6,7,8,9,0,5]
              #Creamos una lista con valores númericos enteros.
print (list_number)
print ()
print("*************************************************************")
print ()
x = list_number.count(5)
                            #Con el metodo count lo que hacemos es mirar cuantas veces se repite 
                            #el valor de nuestra lista está el valor deseado.
print (x)