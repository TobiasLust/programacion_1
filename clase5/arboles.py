import csv
import pprint

FILE = "../Data/arbolado-en-espacios-verdes.csv"


def limpiar_dato(data):
    if "." in data:
        return float(data)
    return int(data)


def leer_arboles(file):
    container = []
    with open(file, encoding="utf-8") as df:
        reader = csv.DictReader(df)
        container = [arbol for arbol in reader]
    return container


def medidas_de_especie(especies, arboleda):
    return {
        especie: [
            (float(arbol["altura_tot"]), float(arbol["diametro"]))
            for arbol in arboleda
            if arbol["nombre_com"] == especie
        ]
        for especie in especies
    }


arboleda = leer_arboles(FILE)

H = [float(arbol["altura_tot"]) for arbol in arboleda]


H_D = [(float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda]

especies = ["Eucalipto", "Palo borracho rosado", "Jacarandá"]

medidas = medidas_de_especie(especies, arboleda)


