def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True

        i += 1
    return False

rta = tiene_a ('palabra')
print(rta)

# Ejercicio 5.1
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    lista_nueva = lista[:]
    invertida = []
    i = len(lista_nueva)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista_nueva.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')