#Este Metodo sirve para eliminar un elemento en especifico de nuestro diccionario.

dictionary = {
    "name" : "Sebas",
    "lastname" : "Rodriguez",
    "password" : 1234567890
}

method = dictionary.pop("password") #Este metodo debe de recibir como parametro una clave.

print(method)
print(dictionary)