import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0
    try:
        with open(nombre_archivo) as file:
            reader = csv.DictReader(file)
            try:
                for row in reader:
                    costo += float(row["precio"])* int(row["cajones"])
            except ValueError:
                pass
    except FileNotFoundError:
        print('No se encuentra el archivo:',nombre_archivo)
    
    return round(costo,2)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)