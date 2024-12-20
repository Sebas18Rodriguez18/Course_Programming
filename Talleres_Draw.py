import os, time

RESET = '\033[0m'
DARK_RED = '\033[31m'
DARK_GREEN = '\033[32m'
DARK_YELLOW = '\033[33m'
DARK_BLUE = '\033[34m'
DARK_MAGENTA = '\033[35m'

# ****************************************************************************************************
# DEFINICIONES
def  menu ():
    os.system ('cls')
    print (f"{DARK_MAGENTA}MENU{RESET}")
    print ()
    print (f"{DARK_BLUE}1. Par o Impar")
    print (f"2. Numero Mayor")
    print (f"3. Año Bisiesto")
    print (f"4. Calificaciones")
    print (f"5. Par o Impar o Cero")
    print (f"6. Rango")
    print (f"7. Edades")
    print (f"8. Multiplos")
    print (f"9. Meses")
    print (f"10. Descuento")
    print (f"11. Dos Digitos")
    print (f"12. Contraseña")
    print (f"13. Velocidad")
    print (f"14. Vestimenta")
    print (f"15. Absoluto")
    print (f"16. Cadenas")
    print (f"17. Semaforo")
    print (f"18. Edad")
    print (f"19. IMC")
    print (f"20. Piedra Papel o Tijeras")
    print (f"21. Examen de German{RESET}")
    print (f"{DARK_RED}22. Finalizar{RESET}")

def parImpar ():
        x = int(input("Ingrese el número "))
        if x % 2 == 0:
            print("PAR")
        elif x % 2 != 0:
            print ("IMPAR")
        else:
            print ("ES CERO")

def numMayor ():
    a = int(input("Digite el primer número "))
    b = int(input("Digite el segundo número "))
    c = int(input("Digite el tercer número "))
    
    if a > b and a > c:
        print(a, "Es mayor")
    elif b > a and b > c:
        print(b, "Es mayor")
    else:
        print(c, "Es mayor")

def anioBisiesto ():
    anio = int(input("Ingresa el año "))
    if anio % 400 == 0 or anio % 4 == 0 and anio % 100 != 0:
        print(anio,"es Bisiesto")
    else:
        print(anio, "no es Bisiesto")

def calificaciones ():
    nota = int(input("Ingrese su nota de 0 a 100"))
    nota >= 0 and nota >= 100
    if nota <= 59:
        print("F")
    else:
        if nota >= 60 and nota <= 69:
            print("D")
        else:
            if nota >= 70 and nota <= 79:
                print("C")
            else:
                if nota >= 80 and nota <= 89:
                    print("B")
                else:
                    print("A")

def pnc ():
    n = int (input("Ingrese un número "))
    if n < 0:
        print (n, "Es negativo")
    elif n > 0:
        print (n, "Es positivo")
    else:
        print (n, "Es cero")

def rango ():
    a = int(input("Ingrese un número "))
    b = int(input("Ingrese el primer número del rango "))
    c = int(input("Ingrese el segundo número del rango "))
    if a >= b and a <= c:
        print (a, "Está dentro del rango")
    else:
        print (a, "No está dentro del rango")

def edades ():
    edad = int(input("Ingrese una edad "))
    edad2 = int(input("Ingrese una segunda edad "))
    if edad > edad2:
        print("La edad de",edad,"es mayor que la edad de", edad2)
    else:
        if edad == edad2:
            print ("La edad de",edad,"es igual a la edad de",edad2)
        else:
            print("La edad de",edad2,"es mayor que la edad de",edad)

def multiplos ():
    a = int (input("Ingrese el primer numero "))
    b = int (input("Ingrese el segundo numero "))
    a > b
    if a % b == 0:
        print(a,"es multiplo de", b)
    else:
        print(a,"no es multiplo de", b)
    b > a
    if b % a == 0:
        print (b,"es multiplo de",a)
    else:
        print (b,"no  es multiplo de",a)

def meses ():
    mes = int(input("Ingrese el numero de un mes "))
    if mes >= 1 and mes <= 12:
        mes_31 = [1, 3, 5, 7, 8, 10, 12]
        mes_30 = [4, 6, 9, 11]
        if mes in mes_31:
            print ("Este mes tiene 31 días.")
        elif mes in mes_30:
            print ("Este mes tiene 30 días.")
        elif mes == 2:
            anio = int(input("Ingrese el año "))
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                print ("Este mes tiene 29 días ya que es bisiesto")
            else:
                print ("Este mes tiene 28 días porque no es bisiesto")
    else:
        print ("ERROR, número de mes inválido.")

def descuento ():
    def calcular_precio_final(producto, descuento, umbral):
        if producto > umbral:
            descuento_aplicado = producto * descuento
            producto = producto - descuento_aplicado
            print(f"El precio final del producto es: {producto}")
        else:
            print("El descuento no aplica")

    producto = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento (en decimal, ej. 0.1 para 10%): "))
    umbral = float(input("Ingrese el umbral para aplicar el descuento: "))

    calcular_precio_final(producto, descuento, umbral)

def dosDigitos ():
    n = int(input("Digite un número "))
    if n < 10:
        print (n,"Tiene solo un digito")
    elif n < 100:
        print (n,"Tiene dos digitos")
    else:
        print (n,"Tiene más de dos digitos")

def contrasenia ():
    contrasenia = (input("Digite su contraseña "))
    predefinida = contrasenia
    os.system ('cls')
    while True:
        contrasenia = (input("Digite su contraseña "))
        os.system ('cls')
        if contrasenia == predefinida:
            os.system ('cls')
            print("Contraseña correcta")
            break
        else:
            os.system ('cls')
            print("Contraseña incorrecta, digitela de nuevo")

def velocidad ():
    velocidad = int(input("Ingrese la velocidad "))
    if velocidad <= 40:
        print ("La velocidad es lenta")
    elif velocidad >= 40 and velocidad <= 60:
        print("La velocidad es normal")
    else:
        print("La velocidad es rápida")

def vestimenta ():
    temp = int(input("Ingrese la temperatura "))
    if temp <= 10:
        print ("Hace mucho frio, usa un abrigo")
    elif temp >= 10 and temp <= 20:
        print ("Hace frio, usa una chaqueta")
    else:
        print ("Hace calor, usa una camiseta")

def absoluto ():
    num = int(input("Ingresa un número "))
    if num >= 0:
        print ("El valor absoluto es",num)
    else:
        num = num * (-1)
        print ("El valor absoluto es",num)

def cadena ():
    a = input("Ingresa una palabra ")
    b = input("Ingresa otra palabra ")
    if b < a:
        print (b,"Es mayor")
    elif a == b:
        print (a,"y",b,"son iguales")
    else:
        print (a,"Es mayor")

def semaforo ():
    color = input("ingrese un color ")
    if color == ("verde") or ("amarillo") or ("rojo"):
        if color == ("verde"):
            print ("Avance")
        elif color == ("amarillo"):
            print ("Preparese para detenerse")
        else:
            print ("Detengase")
    else:
        print ("ERROR")

def edad ():
    edad = int(input("Ingrese una edad "))
    if edad < 4:
        print ("Es un bebe")
    elif edad >= 5 and edad <=13:
        print ("Es un Niño/a")
    else:
        if edad >= 14 and edad <=19:
            print ("Es un/una adolescente")
        elif edad >= 20 and edad <=64:
            print ("Es un/una adulto/a")
        else:
            print ("Es una persona de mayor edad")

def imc ():
    peso = float (input("Ingrese su peso "))
    altura = float (input("Ingrese su altura "))
    imc = peso / (altura ** 2)
    if imc <= 18.50:
        print ("Bajo peso")
    elif imc > 18.50 and imc <= 24.99:
        print ("Normal")
    else:
        if imc > 24.99 and imc <= 29.99:
            print ("Sobrepeso")
        else:
            print ("Obesidad")

def piPati ():
      while True:  
        jugada1 = (str(input("Ingresa la jugada 1 ")))
        os.system ('cls')
        jugada2 = (str(input("Ingresa la jugada 2 ")))
        os.system ('cls')
        if jugada1 == jugada2:
            print("EMPATADOS")
        elif (jugada1 == "piedra" and jugada2 == "tijera") or (jugada1 == "tijera" and jugada2 == "papel") or (jugada1 == "papel" and jugada2 == "piedra"):
            print("GANA", jugada1)
            break
        else:
            print("GANA", jugada2)
            break

def exaGer ():
    num = int(input("Digite un número de dos digitos "))
    if num > 9 and num < 100:
        num_a = num // 10
        num_b = num % 10
        numc = num_a + num_b
        print (num_a)
        print (num_b)
        print ("La suma de ambos números es: ", numc)
        if numc % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    else:
        print("ERROR, ingrese otro número de dos digito")

# **************************************************************************************************
opcion = 0
while opcion != 22:
    menu ()
    opcion = int(input(f"{DARK_YELLOW}Selecciona una opcion: {RESET}"))
    if opcion == 1:
        os.system ('cls')
        parImpar ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 2:
        os.system ('cls')
        numMayor ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 3:
        os.system ('cls')
        anioBisiesto ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 4:
        os.system ('cls')
        calificaciones ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 5:
        os.system ('cls')
        pnc ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 6:
        os.system ('cls')
        rango ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 7:
        os.system ('cls')
        edades ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 8:
        os.system ('cls')
        multiplos ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 9:
        os.system ('cls')
        meses ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 10:
        os.system ('cls')
        descuento ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 11:
        os.system ('cls')
        dosDigitos ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 12:
        os.system ('cls')
        contrasenia ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 13:
        os.system ('cls')
        velocidad ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 14:
        os.system ('cls')
        vestimenta ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 15:
        os.system ('cls')
        absoluto ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 16:
        os.system ('cls')
        cadena ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 17:
        os.system ('cls')
        semaforo ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 18:
        os.system ('cls')
        edad ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 19:
        os.system ('cls')
        imc ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 20:
        os.system ('cls')
        piPati ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 21:
        os.system ('cls')
        exaGer ()
        print ()
        input (f"{DARK_RED}ENTER para continuar: {RESET}")
    elif opcion == 22:
        for i in range (5, 0, -1):
            os.system ('cls')
            print (f"{DARK_RED}Finalizará en {i} segundos{RESET}")
            time.sleep (1)
os.system ('cls')
print (f"{DARK_GREEN}Haz salido del sistema correctamente{RESET}")