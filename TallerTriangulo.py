"""
Análisis de Triángulos.

Funciones:
    1. Entrada de coordenadas: Solicita al usuario las coordenadas (x, y) de tres puntos.
    2. Identificación de cuadrantes: Determina en qué cuadrante del plano cartesiano se 
    encuentra cada punto.
    3. Cálculo de distancias: Calcula la distancia entre cada par de puntos (AB, BC, CA).
    4. Verificación de triángulo: Comprueba si los tres puntos pueden formar un triángulo válido.
    5. Análisis del triángulo: Si es válido, el programa:
        - Clasifica el triángulo (equilátero, isósceles o escaleno).
        - Calcula el perímetro y el área del triángulo.
        - Determina si el triángulo es rectángulo.
       De no ser válido el script se cerrará.
Notas:
    - El programa utiliza la desigualdad triangular para verificar si los puntos forman un triángulo válido.
    - Para determinar si es un triángulo rectángulo, se usa el teorema de Pitágoras con una pequeña
    tolerancia para manejar errores de punto flotante.
    - Este Script usa la fórmula de Herón para calcular el área del triángulo.
"""

#INICIO DEL PROGRAMA...

#COORDENADAS
import os, time
os.system ('cls')
print("#COORDENADAS DEL PUNTO 1")
print()
x1 =  float(input("Digite la coordenada X del punto 1: "))
y1 =  float(input("Digite la coordenada Y del punto 1: "))
print()
print("#COORDENADAS DEL PUNTO 2")
print()
x2 =  float(input("Digite la coordenada X del punto 2: "))
y2 =  float(input("Digite la coordenada Y del punto 2: "))
print()
print("#COORDENADAS DEL PUNTO 3")
print()
x3 =  float(input("Digite la coordenada X del punto 3: "))
y3 =  float(input("Digite la coordenada Y del punto 3: "))

#IDENTIFICAMOS SU CUADRANTE

print()
print("#IDENTIFICAMOS SU CUADRANTE")
print()
def cuadrantes (x, y):
    if x > 0 and y > 0:
        print (f"El punto ({x},{y}) está en el cuadrante I")
    elif x < 0 and y < 0:
        print (f"El punto ({x},{y}) está en el cuadrante III")
    elif x == 0 and y == 0:
        print (f"El punto ({x},{y}) está en el origen")
    elif x > 0 and y < 0:
        print (f"El punto ({x},{y}) está en el cuadrante IV")
    elif x == 0:
        print (f"El punto ({x},{y}) está en el eje Y")
    elif x < 0 and y > 0:
        print (f"El punto ({x},{y}) está en el cuadrante II")
    else:
        print (f"El punto ({x},{y}) está en el eje X")
cuadrantes (x1, y1)
cuadrantes (x2, y2)
cuadrantes (x3, y3)

#DISTANCIAMIENTO ENTRE LOS PUNTOS

print()
print("#DISTANCIAMIENTO ENTRE LOS PUNTOS")
print()

def distancia (x1, y1, x2, y2):
    ax = x2 - x1
    bx = y2 - y1
    lado = ((ax**2) + (bx**2)) ** 0.5
    return lado
lado_1 = distancia(x1, y1, x2, y2)
lado_2 = distancia(x2, y2, x3, y3)
lado_3 = distancia(x3, y3, x1, y1)
print ("La distancia entre el punto 1 y 2 mide: ", round(lado_1))
print ("La distancia entre el punto 2 y 3 mide: ", round(lado_2))
print ("La distancia entre el punto 3 y 1 mide: ", round(lado_3))

#DESIAGUALDAD TRIANGULAR

print()
print("#DESIGUALDAD TRIÁNGULAR")
print()

if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_3 + lado_1 > lado_2:
    print (f"Los lados del triángulo miden ({round(lado_1)}), ({round(lado_2)}), ({round(lado_3)})")
    
    def casi_igual (a, b, tolerancia = 1e-9):
        return abs (a - b) < tolerancia

    def tipo_triangulo (lado_1, lado_2, lado_3):
        if casi_igual (lado_1, lado_2) and casi_igual (lado_2, lado_3):
            return "Equilátero"
        elif casi_igual (lado_1, lado_2) or casi_igual (lado_1, lado_3) or casi_igual (lado_3, lado_2):
            return "Isósceles"
        else:
            return "Escaleno"
    tipo = tipo_triangulo (lado_1, lado_2, lado_3)
    print (f"Los lados del triangulo forman un triángulo {tipo}")

    #CALCULO DEL PERIMETRO Y EL AREA

    print()
    print("#CALCULO DEL PERIMETRO Y EL AREA DEL TRIÁNGULO")
    print()
    perimetro = lado_1 + lado_2 + lado_3
    print ("El perimetro del tráingulo es",(round(perimetro)))
    s = (lado_1 + lado_2 + lado_3)/2
    area = (s * (s - lado_1) * (s - lado_2) * (s - lado_3))**0.5
    print ("El área del  triángulo es ",(round(area)))

    #DETERMINAR SI ES UN TRIANGULO RECTANGULO

    print()
    print("#DETERMINAR SI ES UN TRIÁNGULO RECTANGULO")
    print()
    lados = sorted([lado_1, lado_2, lado_3])
    a, b, c = lados
    if abs(a**2 + b**2 - c**2) < 1e-6:
        print("Es un triángulo rectángulo")
    else:
        print("No es un triángulo rectángulo")
else:
    print("No es un triángulo")
print ()