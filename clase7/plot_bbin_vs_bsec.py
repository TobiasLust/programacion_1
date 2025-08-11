import random
import matplotlib.pyplot as plt
import numpy as np

def busqueda_secuencial_comps(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria_comps(lista, n):
    izq = 0
    der = len(lista) - 1
    comps = 0

    while izq <= der:
        medio = (izq + der) // 2

        comps += 1
        if lista[medio] == n:
            return medio, comps

        comps += 1
        if lista[medio] > n:
            der = medio - 1
        else:
            izq = medio + 1

    return -1, comps


def generar_lista(n, m):
    l = random.sample(range(m), k=n)
    l.sort()
    return l


def generar_elemento(m):
    return random.randint(0, m - 1)


m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()


def busqueda_secuencial_comps(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0  # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i, z in enumerate(lista):
        comps += 1  # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria_comps(lista, n):
    '''Si n está en la lista devuelve su índice, sino -1, y la cantidad de
    comparaciones que hace la búsqueda binaria.
    '''
    izq = 0
    der = len(lista) - 1
    comps = 0

    while izq <= der:
        medio = (izq + der) // 2
        comps += 1  # comparación con ==
        if lista[medio] == n:
            return medio, comps
        comps += 1  # comparación con >
        if lista[medio] > n:
            der = medio - 1
        else:
            izq = medio + 1
    return -1, comps


def generar_lista(n, m):
    '''Genera una lista ordenada de n elementos distintos en rango [0, m).'''
    l = random.sample(range(m), k=n)
    l.sort()
    return l


def generar_elemento(m):
    '''Genera un elemento aleatorio en rango [0, m).'''
    return random.randint(0, m - 1)


def experimento_secuencial_promedio(lista, m, k):
    '''Devuelve el promedio de comparaciones de la búsqueda secuencial en k pruebas.'''
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        _, c = busqueda_secuencial_comps(lista, x)
        comps_tot += c
    return comps_tot / k


def experimento_binario_promedio(lista, m, k):
    '''Devuelve el promedio de comparaciones de la búsqueda binaria en k pruebas.'''
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        _, c = busqueda_binaria_comps(lista, x)
        comps_tot += c
    return comps_tot / k


def graficar_bbin_vs_bseq(m, k):
    '''Genera el gráfico comparativo de búsquedas secuencial y binaria.

    Parámetros:
    - m: rango de los elementos (0 a m-1).
    - k: cantidad de experimentos por tamaño de lista.
    '''
    largos = np.arange(1, 257)
    comps_seq = np.zeros_like(largos, dtype=float)
    comps_bin = np.zeros_like(largos, dtype=float)

    for i, n in enumerate(largos):
        lista = generar_lista(n, m)
        comps_seq[i] = experimento_secuencial_promedio(lista, m, k)
        comps_bin[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos, comps_seq, label='Búsqueda Secuencial')
    plt.plot(largos, comps_bin, label='Búsqueda Binaria')
    plt.xlabel('Largo de la lista')
    plt.ylabel('Comparaciones promedio')
    plt.title('Comparación: Búsqueda Secuencial vs Binaria')
    plt.legend()
    plt.xlim(1, 256)
    plt.ylim(0, max(comps_seq.max(), comps_bin.max()) * 1.1)
    plt.show()


# Parámetros de ejecución por defecto
m = 10000  # rango de valores posibles
k = 1000   # número de pruebas por tamaño de lista
graficar_bbin_vs_bseq(m, k)
