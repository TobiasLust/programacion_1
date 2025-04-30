import csv

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




camion = leer_camion('../Data/camion.csv')
costo = sum([float(s['cajones'])* float(s['precio']) for s in camion])
print(costo)

precios = leer_precios('../Data/precios.csv')
valor = sum([float(s['cajones']) * float(precios[s['nombre']]) for s in camion])
print(valor)

mas_100 = [s for s in camion if float(s['cajones']) > 100]
print(mas_100)