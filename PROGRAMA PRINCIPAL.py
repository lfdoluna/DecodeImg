# El siguiente código de programación permite el procesamiento digital de una imagen, la cual al ser analizada es convertida en
#sus modalidades: escala de grises y binaria, con la finalidad de saber el valor de cada pixel de la imagen

"""
Created on Wed Sep  7 03:12:26 2022

@author: José Manuel Trejo Molina
"""

#Se importa la libreria OpenCV, la cual sirve para leer imagenes
import cv2
#Se importa la libreria NUMPY, la cual sirve para representar las imagenes como matrices
import numpy as np
#Se leé la imagen
imagen=cv2.imread('FIRULAIS.jpg')
#Se convierte la imagen de RGB a escala de grises
imgGris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#Se convierte la imagen escala de grises a binaria utilizando el metodo OTSU
umbral,imagenMetodo= cv2.threshold (imgGris,0,255,cv2.THRESH_OTSU)
#Se introducen las dimensiones de la imagen binaria, y obtiene los datos de cada pixel de la misma
for fila in range (360):
    for columna in range (360):
        print("Coordenada", "X", + fila, "Y", + columna, "=", str(imagenMetodo[fila,columna]))

img=cv2.imread('FIRULAIS.jpg')
    
#se invierten los colores de la imagen binaria
inverted_imagenMetodo = np.invert(imagenMetodo)
#Se muestra la imagen
cv2.imshow('IMAGEN BINARIA', imagenMetodo)

#se crean las ventanas de visualización de las imagenes
cv2.waitKey(0)
#Se cierran todas las ventanas
cv2.destroyAllWindows() 