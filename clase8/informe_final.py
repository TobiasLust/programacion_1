from fileparse import parse_csv


def leer_camion(iterador):

    camion_lst = parse_csv(iterador, types=[str, int, float])
    return camion_lst


def leer_precios(iterador):

    precios = parse_csv(iterador, types=[str, float], has_headers=False)
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


def f_principal(param: list):
    camion = leer_camion(param[1])
    precios = leer_precios(param[2])
    informe_camion(camion, precios)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        f_principal(sys.argv)
