import csv

DATA = '../Data/camion.csv' # import data del camion: nombre cajones precio

with open(DATA) as file:
    reader = csv.DictReader(file)
    headers = ['Producto','Cajones','Precio']


    print(f'{headers[0]} {headers[1]} {headers[2]}')

    for row in reader:
        print(f'{row["nombre"]} {row["cajones"]} {row["precio"]}')

    
