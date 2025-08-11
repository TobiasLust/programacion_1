from informe_funciones import leer_camion


def costo_camion(nombre_archivo):
    costo_total = 0

    camion = leer_camion(nombre_archivo)
    
    for row in camion:
        costo_total += row['cajones'] * row['precio']
    
    return costo_total

costo_total_camion = costo_camion('../Data/camion.csv')
print(costo_total_camion)