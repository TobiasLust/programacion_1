def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos


busqueda_lineal([1, 4, 54, 3, 0, -1], 44)

busqueda_lineal([1, 4, 54, 3, 0, -1], 3)

busqueda_lineal([1, 4, 54, 3, 0, -1], 0)

busqueda_lineal([], 42)