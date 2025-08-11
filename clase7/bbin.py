lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

## log2(n)
def busq_binaria(lista, n):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == n:
            return medio
        elif lista[medio] > n:
            der = medio - 1
        else:
            izq = medio + 1

    return -1


def donde_insertar(lista,n):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == n:
            return medio
        elif lista[medio] > n:
            der = medio - 1
        else:
            izq = medio + 1

    return lista,medio


def insertar(lista,n):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == n:
            return medio
        elif lista[medio] > n:
            der = medio - 1
        else:
            izq = medio + 1

    lista.insert(izq,n)
    return izq

