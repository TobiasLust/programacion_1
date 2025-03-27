import csv
from collections import Counter

def main():
    camion = leer_camion('../Data/camion.csv')
    camion2 = leer_camion('../Data/camion2.csv')
    tenencias_1 = get_counter(camion)
    tenencias_2 = get_counter(camion2)

    tenencia_total = tenencias_1 + tenencias_2
    print(tenencia_total)
    

def leer_camion(data_camion):
    camion = []

    try:
        with open(data_camion) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["precio"] = float(row["precio"])
                row["cajones"] = int(row["cajones"])
                camion.append(row)

    except FileNotFoundError:
        print(f"{data_camion} archivo no encontrado")

    return camion

def get_counter(camion):
    tenencias = Counter()
    for row in camion:
        tenencias[row["nombre"]] += row["cajones"]
    
    return tenencias


main()
