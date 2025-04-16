def propagar(lista:list) -> list :
    fosforos = lista[:]
    fosforo = 0

    for i,e in enumerate(fosforos):
        if e == 0 and fosforo == 1:
            fosforos[i] = 1
        fosforo = fosforos[i]
    return fosforos

fosforos_sp = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
propagado = propagar(fosforos_sp)
print(fosforos_sp,propagado)
