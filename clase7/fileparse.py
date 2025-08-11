# fileparse.py
import csv


def parse_csv(nombre_archivo, select=None, types=None,has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        registros = []
        # Lee los encabezados
        if not has_headers:
            for row in rows:
                if not any(field.strip() for field in row):  # Salta fila sin datos
                    continue
                
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                
                registros.append(tuple(row))

            return registros
            


        headers = next(rows)

        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []

        for row in rows:
            if not any(field.strip() for field in row):  # Salta fila sin datos
                continue
            if indices:
                row = [row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

