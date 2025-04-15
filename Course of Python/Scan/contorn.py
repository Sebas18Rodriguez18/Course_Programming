import cv2 #Importar la libreria de OpenCV

#Leer la imagen
image = cv2.imread(r'c:\Users\Sebas\repos\Course_Programming\Course of Python\Scan\contorno.png')

#Convertir a escala de grises
greys = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Aplicar un filtro umbra
_, umbral = cv2.threshold(greys, 100, 255, cv2.THRESH_BINARY)

#Aplicar un filtro de desenfoque gaussiano
contorn, hierarchy = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Dibujar contornos en la imagen original
cv2.drawContours(image, contorn, 1, (251, 60, 0), 3)


#Mostrar la imagen
cv2.imshow('Hello i am original image', image)
cv2.imshow('Hello i am grey image', greys)
cv2.imshow('Hello i am a umbral image', umbral)

cv2.waitKey(0) #Esperar a que se presione una tecla
cv2.destroyAllWindows() #Cerrar todas las ventanas