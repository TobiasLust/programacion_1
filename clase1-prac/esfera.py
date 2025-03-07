'''
En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que 
le pida a le usuarie que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. 
Sugerencia: recordar que el volumen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para responder 
¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603.

'''

import math

radio = input("Ingrese el radio de la esfera: ")

volumen = 4/3 * math.pi * float(radio) ** 3
print(f"El volumen de la esfera es: {volumen}")
        

