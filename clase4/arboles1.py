import csv
from collections import Counter

FILE = "../Data/arbolado-en-espacios-verdes.csv"


def main():
    df = leer_parque(file=FILE,parque='GENERAL PAZ')
    print("Cantidad de arboles:\n",len(df))
    especies = obtener_especies(df)
    print("\nEspecies:\n",especies)
    ejemplares = contar_ejemplares(df)
    print("\nLas 5 especies mas comunes \n",ejemplares.most_common(5))

def leer_parque(file, parque=None):
    """
    Generar una lista de diccionarios con la informacion de
    cada arbol  que se encuentra en el parametro 'parque'.
    Si no se le pasa un argumento al parametro 'parque' genera
    una lista con todos los arboles del archivo csv
    """

    arboles_list = []

    try:
        with open(file) as arboles_csv:
            reader = csv.DictReader(arboles_csv)

            # Si no se le pasa argumento a la funcion
            if parque == None:
                for row in reader:
                    arboles_list.append(row)
                return  arboles_list

            for row in reader:
                if row["espacio_ve"] == parque:
                    arboles_list.append(row)
            
            return arboles_list


    except FileNotFoundError:
        print(f"Error: No se encontro '{file}'")

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


def obtener_alturas(list_arboles,especie):
    ...



    

main()
