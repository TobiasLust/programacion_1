import csv

DATA = '../Data/camion.csv' # import data del camion: nombre cajones precio


def main():
   costo_total_camion = costo_camion(DATA)
   print(f"Costo total del camion: {costo_total_camion}") 

def costo_camion(data_camion):
    costo_total = 0
    with open(data_camion) as file:
        reader = csv.DictReader(file)

        for row in reader:
            costo_total += float(row["precio"]) * int(row["cajones"])

    
    return costo_total

main()