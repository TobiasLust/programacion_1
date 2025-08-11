import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import pprint

FILE = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')


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


def scatter_hd(lista_de_pares):
    vector = np.array(lista_de_pares)
    d = vector[:,1]
    h = vector[:,0]
    plt.scatter(d,h,alpha=0.5)
    plt.xlabel('diametro (cm)')
    plt.ylabel('alto (m)')
    plt.title('Relacion diametro-alto para Jacarandas')
    plt.show()


arboleda = leer_arboles(FILE)

# Histograma de las alturas de los Jacarandá en la comuna 14 de CABA
medida = medidas_de_especie(['Jacarandá'],arboleda)
altos = [altura for altura,diametro in medida['Jacarandá']]
plt.hist(altos,bins=25)
plt.show()


# Grafico de dispersion de cuanto crece en altura arboles en funcion de su diametro
scatter_hd(medida["Jacarandá"])

especies= ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especie(especies,arboleda)

for especie,hd_list in medidas.items():
    vector = np.array(hd_list)
    d = vector[:,1]
    h = vector[:,0]
    plt.scatter(d,h,alpha=0.7,label=especie)
    


plt.xlabel('diametro (cm)')
plt.ylabel('alto (m)')
plt.ylim(0,70)
plt.title(f'Relacion diametro-alto entre especies')
plt.legend()
plt.show()