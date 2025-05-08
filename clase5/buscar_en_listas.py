def buscar_u_elemento(lista,e):
    index = -1
    for i,elem in enumerate(lista):
        if elem == e:
            index = i
    
    return index

def buscar_n_elemento(lista,e):
    rep = 0
    for elem in lista:
        if elem == e:
            rep += 1
    
    return rep


def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    if lista:
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e < 0:
                return 'Hay numeros negativos'
            if e > m:
                m = e
        return m
    return 'Lista esta vacia'
        


indice = buscar_u_elemento([1,2,3,2,3,4],3)
rep= buscar_n_elemento([1,2,3,2,3,4],3)
n_max = maximo([1,2,3,2,3,4])



print(indice)
print(rep)
print(n_max)
