import cv2 #Importar libreria de OpenCV
import numpy as np #Importar libreria de matrices

#Parametros de Filtros
valorGauss = 3
valorKernel = 5

#Cargar Imagen
originalOne = cv2.imread(r'c:\Users\Sebas\repos\Course_Programming\Course of Python\Scan\monedas.jpg' o 'nombre de la imagen dentro de la misma carpeta')
originalTwo = cv2.imread(r'c:\Users\Sebas\repos\Course_Programming\Course of Python\Scan\monedassoles.jpg' o 'nombre de la imagen dentro de la misma carpeta')

#Filtros de Imagen
grey1 = cv2.cvtColor(originalOne, cv2.COLOR_BGR2GRAY)
grey2 = cv2.cvtColor(originalTwo, cv2.COLOR_BGR2GRAY)
noise1 = cv2.GaussianBlur(grey1, (valorGauss, valorKernel), 0)
noise2 = cv2.GaussianBlur(grey2, (valorGauss, valorKernel), 0)
canny1 = cv2.Canny(noise1, 60, 100)
canny2 = cv2.Canny(noise2, 60, 100)

#Morphology
#Se utiliza para eliminar el ruido de la imagen y mejorar la detección de contornos
kernel = np.ones((valorKernel, valorKernel), np.uint8)
closing1 = cv2.morphologyEx(canny1, cv2.MORPH_CLOSE, kernel)
closing2 = cv2.morphologyEx(canny2, cv2.MORPH_CLOSE, kernel)

#Dibujar Contornos
#cv2.findContours() devuelve una lista de contornos encontrados en la imagen
contorn1, hierarchy = cv2.findContours(closing1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contorn2, hierarchy = cv2.findContours(closing2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Muestra el total de contornos encontrados
#cv2.drawContours() dibuja los contornos encontrados en la imagen original
print('Total de Monedas de la imagen 1: {}'.format(len(contorn1)))
print('Total de Monedas de la imagen 2: {}'.format(len(contorn2)))

#Dibujar contornos en la imagen original
cv2.drawContours(originalOne, contorn1, -1, (0, 255, 0), 2)
cv2.drawContours(originalTwo, contorn2, -1, (0, 255, 0), 2)


#Mostrar Resultados
# cv2.imshow('Grey', grey)
# cv2.imshow('Noise', noise)
# cv2.imshow('Canny', canny)
# cv2.imshow('Morphology', closing)
cv2.imshow('originalOne', originalOne)
cv2.imshow('originalTwo', originalTwo)
cv2.waitKey(0) #Esperar a que se presione una tecla
cv2.destroyAllWindows() #Cerrar todas las ventanas
