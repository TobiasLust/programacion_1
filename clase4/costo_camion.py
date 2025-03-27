import csv
DATA = '../Data/fecha_camion.csv'

def costo_camion(camion_data):
    costo_total = 0

    with open(camion_data) as file:
        reader = csv.DictReader(file)

        for i,row in enumerate(reader,start=1):
            try:
                costo_total += float(row["precio"]) * int(row["cajones"])
            except ValueError:
                print(f'Fila {i}: No puede interpretar: {row}')
                continue
    
    return costo_total

costo_total_camion = costo_camion(DATA)
print(costo_total_camion)