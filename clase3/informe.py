import csv

'''
Usando este código como guía, creá un nuevo archivo informe.py. 
En este archivo, definí una función leer_camion(nombre_archivo) que abre un archivo 
con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas.
 Para hacerlo vas a tener que hacer algunas modificaciones menores al código de arriba.
'''

def main():
    precios_camion = leer_camion("../Data/camion.csv")
    precios_venta = leer_precios("../Data/precios.csv")
    print(f'Balance: ${calc_balance(precios_camion,precios_venta)}')

def leer_camion(nombre_archivo):

    camion_lst = []
    
    try:
        with open(nombre_archivo) as file:
            reader = csv.DictReader(file)
            for row in reader:
                camion_lst.append(row)
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no se encontro')
        return []
    
    return camion_lst

def leer_precios(nombre_archivo):

    precios = {}
    
    try:
        with open(nombre_archivo) as file:
            reader = csv.reader(file)
            
            for row in reader:
                try:
                    nombre,precio = row
                    precios[nombre] = precio
                except ValueError:
                    continue
                
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no se encontro')
        return
    
    return precios

def calc_balance(precios_camion,precios_venta):
    balance = 0
    for producto in precios_camion:
        cajones = int(producto["cajones"])
        compra = float(producto["precio"]) * cajones
        venta = float(precios_venta[producto["nombre"]]) * cajones
        balance += venta - compra

    return round(balance,2)


main()