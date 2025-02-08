#Este Metodo sirve para devolver el valor de una clave de nuestro diccionario.

dictionary = {
    "name" : "Sebas",
    "lastname" : "Rodriguez",
    "password" : 1234567890
}

method = dictionary.get("lastname") #Este metodo debe de recibir como parametro una clave.

print(method)