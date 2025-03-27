import csv


def main():
    precios_camion = leer_camion("../Data/camion.csv")
    precios_venta = leer_precios("../Data/precios.csv")
    informe = crear_informe(camion=precios_camion,precios=precios_venta)
    crear_tabla(informe)




def leer_camion(nombre_archivo):

    camion_lst = []

    try:
        with open(nombre_archivo) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["cajones"]=int(row["cajones"])
                row["precio"]= float(row["precio"])
                camion_lst.append(row)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontro")

    return camion_lst


def leer_precios(nombre_archivo):

    precios = {}

    try:
        with open(nombre_archivo) as file:
            reader = csv.reader(file)

            for row in reader:
                try:
                    nombre, precio = row
                    precios[nombre] = float(precio)
                except ValueError:
                    continue

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontro")

    return precios


def crear_informe(camion,precios):
    informe = []

    for row in camion:
        cambio = precios[row['nombre']] - row['precio']
        producto = {'nombre':row['nombre'],
                    'cajones':row["cajones"],
                    'precio':row["precio"],
                    'cambio': cambio}
        informe.append(producto)

    return informe


def crear_tabla(informe):
    headers = tuple(informe[0].keys())
    print(f'    {headers[0]}    {headers[1]}     {headers[2]}     {headers[3]}')
    print('---------- ---------- ---------- ----------')
    for row in informe:
        print(f'{row["nombre"]:>10s} {row["cajones"]:>10d} {"$"+str(row["precio"]):>10s} {row["cambio"]:>10.2f}')


main()
