#En este se mostrará el funcionamiento del metodo append en una lista.

list_number = [1,2,3,4,5,6,7,8,9,0]
              #Creamos una lista con valores númericos enteros.
print (list_number)
print ()
print("*************************************************************")
print ()
list_number.append(35)
              #Con el metodo append lo que hacemos es agregarle un valor más a nuestra lista.
print (list_number)
              #De esta manera pudimos agregarle un valor númerico entero a nuestra lista, 
              #ahora vamos con valores no enteros.

list_number.append("apple")
list_number.append(3.5)
              #En esta parte estamos intentando agregarle datos double o float y 
              #un dato String a nuestra lista.
print ()
print("*************************************************************")
print ()
print (list_number)