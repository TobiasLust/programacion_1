import csv
from collections import Counter

FILE = "../Data/arbolado-en-espacios-verdes.csv"


def main():
    try:
        df = leer_parque(file=FILE, parque="ANDES, LOS")
    except ValueError as e:
        print(e)
        return
    except TypeError:
        print("Falta argumento 'parque'")

    print("Cantidad de arboles:\n", len(df))

    especies = obtener_especies(df)

    print("\nEspecies:\n", especies)

    ejemplares = contar_ejemplares(df)

    print("\nLas 5 especies mas comunes \n", ejemplares.most_common(5))

    altura_max, altura_prom = obtener_alturas(df, "Jacarandá")

    print(f"Altura max: {altura_max}\nAltura prom: {altura_prom}")

    inclinaciones = obtener_inclinaciones(df, "Jacarandá")

    print(f"Inclinaciones: {inclinaciones}\n")

    especie_max_inclinada = especimen_mas_inclinado(df)
    print("Arbol con mayor inclinacion: ", especie_max_inclinada)

    especie_prom_inclinada = especie_promedio_mas_inclinada(df)
    print("Promedio de inclinacion de la especie: ", especie_prom_inclinada)


def leer_parque(file, parque):

    arboles_list = []

    try:
        with open(file, encoding="utf-8") as arboles_csv:
            reader = csv.DictReader(arboles_csv)

            for row in reader:
                for key in [
                    "long",
                    "lat",
                    "altura_tot",
                    "diametro",
                    "inclinacio",
                    "id_especie",
                    "coord_x",
                    "coord_y",
                ]:
                    row[key] = limpiar_tipo(row[key])

                arboles_list.append(row)

    except FileNotFoundError:
        print(f"Error: No se encontro '{file}'")

    if arboles_list:
        arboles_filtrados = [
            arbol for arbol in arboles_list if arbol["espacio_ve"] == parque
        ]

        # Si no existe parque en el csv
        if not arboles_filtrados:
            raise ValueError("No se encontro el parque especificado.")
        return arboles_filtrados

    # Si el csv esta vacio

    raise ValueError("El archivo CSV está vacío.")


def obtener_especies(list_arboles):
    set_especies = set()
    for arbol in list_arboles:
        set_especies.add(arbol["nombre_com"])

    return set_especies


def contar_ejemplares(list_arboles):
    especies = []

    for arbol in list_arboles:
        especies.append(arbol["nombre_com"])

    return Counter(especies)


def obtener_alturas(list_arboles, especie):
    alturas = []
    for arbol in list_arboles:
        if arbol["nombre_com"] == especie:
            alturas.append(arbol["altura_tot"])

    altura_max = max(alturas)
    altura_prom = sum(alturas) / len(alturas)

    return altura_max, altura_prom


def obtener_inclinaciones(list_arboles, especie):
    inclinaciones = []
    for arbol in list_arboles:
        if arbol["nombre_com"] == especie:
            inclinaciones.append(arbol["inclinacio"])

    return sorted(inclinaciones)


def especimen_mas_inclinado(list_arboles):
    especies = obtener_especies(list_arboles)
    inclinaciones_max = Counter()

    for especie in especies:

        inclinaciones = obtener_inclinaciones(list_arboles, especie)
        inclinacion_max = max(inclinaciones)
        inclinaciones_max[especie] = inclinacion_max

    return inclinaciones_max.most_common(1)


def especie_promedio_mas_inclinada(list_arboles):

    especies = obtener_especies(list_arboles)
    inclinaciones_prom = Counter()

    for especie in especies:
        inclinaciones = obtener_inclinaciones(list_arboles, especie)
        inclinacion_prom = sum(inclinaciones) / len(inclinaciones)
        inclinaciones_prom[especie] = inclinacion_prom

    return inclinaciones_prom.most_common(1)


def limpiar_tipo(num):
    if "." in num:
        return float(num)
    return int(num)


main()
