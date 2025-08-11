import numpy as np
import random
import matplotlib.pyplot as plt

FIGURITAS = 670  # Cantidad total de figuritas para llenar el album
PAQUETE = 5  # Cantidad total de figuritas aleatorias que vienen en los paquetes


def crear_album(figus_total: int):
    """
    Devuelve un vector con una cantidad de ceros
    por figus_total
    """
    return np.zeros(figus_total, dtype=int)


def album_incompleto(album):
    """
    Si el album esta incomple nos regresa TRUE
    """
    if 0 in album:
        return True
    return False


def comprar_paquete(figus_paquete: int, figus_total: int):
    """
    Genera una lista de figus_paquete numeros aleatorios entre 1 y figus_total
    """
    paquete = []
    for _ in range(figus_paquete):
        paquete.append(random.randint(1, figus_total))
    return paquete


def cuantos_paquetes(figus_paquete: int, figus_total: int):
    """
    Devuelve un numero entero con la cantidad de paquetes que se tuvieron
    que comprar hasta que se lleno el album
    """
    paquetes = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_paquete, figus_total)
        for figu in paquete:
            album[figu - 1] += 1
        paquetes += 1

    return paquetes


def experimento_figus(n_repeticiones: int, figus_paquete: int, figus_total: int):

    paquetes_totales = []

    for _ in range(n_repeticiones):
        paquetes_necesarios = cuantos_paquetes(figus_paquete, figus_total)
        paquetes_totales.append(paquetes_necesarios)

    print(
        f"""Para llenar {n_repeticiones} álbumes con un total de {figus_total} figuritas para completar
comprando paquetes de {figus_paquete} figuritas c/u. En promedio se necesitan: {np.mean(paquetes_totales):.2f} paquetes"""
    )


experimento_figus(1000, PAQUETE, FIGURITAS)

