from fileparse import parse_csv


def leer_camion(nombre_archivo):

    camion_lst = parse_csv(nombre_archivo, types=[str, int, float])
    return camion_lst


def leer_precios(nombre_archivo):

    precios = parse_csv(nombre_archivo, types=[str, float], has_headers=False)
    return dict(precios)


def imprimir_tabla(informe):
    headers = tuple(informe[0].keys())
    print(f"    {headers[0]}    {headers[1]}     {headers[2]}     {headers[3]}")
    print("---------- ---------- ---------- ----------")
    for row in informe:
        print(
            f'{row["nombre"]:>10s} {str(row["cajones"]):>10s} {"$"+str(row["precio"]):>10s} {row["cambio"]:>10.2f}'
        )


def crear_informe(camion, precios):
    informe = []

    for row in camion:
        cambio = precios[row["nombre"]] - row["precio"]
        producto = {
            "nombre": row["nombre"],
            "cajones": row["cajones"],
            "precio": row["precio"],
            "cambio": cambio,
        }
        informe.append(producto)

    return informe


def informe_camion(camion, precios):
    informe = crear_informe(camion, precios)
    imprimir_tabla(informe)


camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe_camion(camion,precios) ##### Llamada Funcion