def invertir_lista(lista):
    invertida = []
    len_lista = len(lista) - 1
    for i in range(len_lista, -1, -1):
        invertida.append(lista[i])

    return invertida


print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(["Bogotá", "Rosario", "Santiago", "San Fernando", "San Miguel"]))
