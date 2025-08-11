from informe_final import leer_camion


def costo_camion(nombre_archivo):
    costo_total = 0

    camion = leer_camion(nombre_archivo)

    for row in camion:
        costo_total += row["cajones"] * row["precio"]

    return costo_total


def f_principal(param: list):
    costo_total_camion = costo_camion(param[1])
    print('Costo total:',costo_total_camion)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        f_principal(sys.argv)
