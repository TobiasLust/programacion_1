#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.5. Función tiene_a()
#Comentario: El error del codigo anterior sucedia cuando recorrias caracter por caracter
# podrias encontrarte con algun caracter considerado como uppercase entonces al comparar 'a'
# que se encuentra en lowercase entonces al compararse la misma letra pero diferente case nos daba false
#    Lo corregí transformando la expresion a minusculas usando el metodo lower
# tambien considere que se podria optimizar el codigo ya que in recorre el str sin la necesidad de estar en el anterior bucle while
#    A continuación va el código corregido

def tiene_a(expresion):
    if 'a' in expresion.lower():
        print(expresion,'tiene a')
        return True
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')




#Ejercicio 3.9. Función leer_camion()
#Comentario: El error del codigo se genera ya que registro se encuentra fuer del bucle al intentar
#cuando lo agregamos a la lista lo que en realidad estamos agregando es la referencia a ese dict y entonces al sobreescribir el registro
#fuera del bucle estamos cambiando todas las referencias dentro de la lista
#    Lo corregí simplemente agregando el dict registro dentro del bucle, lo que hace que registro en cada iteracion se "cree" y no se almacene en memoria la var registro
#    A continuación va el código corregido


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)