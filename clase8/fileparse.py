# fileparse.py
import csv


def parse_csv(iterador, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")

    rows = csv.reader(iterador)
    registros = []
    # Lee los encabezados
    if not has_headers:
        for i, row in enumerate(rows):
            if not any(field.strip() for field in row):  # Salta fila sin datos
                continue
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                registros.append(tuple(row))
            except ValueError as e:
                print(f"Fila {i+1}: No pude convertir {row}")
                print(f"Fila {i+1}: Motivo: {e}")

        return registros

    headers = next(rows)

    if select:
        indices = [headers.index(nombre_columna) for nombre_columna in select]
        headers = select
    else:
        indices = []

    for i, row in enumerate(rows):
        if not any(field.strip() for field in row):  # Salta fila sin datos
            continue
        if indices:
            row = [row[index] for index in indices]
        try:
            if types:
                row = [func(val) for func, val in zip(types, row)]

                registro = dict(zip(headers, row))
                registros.append(registro)
        except ValueError as e:
            print(f"Fila {i+1}: No pude convertir {row}")
            print(f"Fila {i+1}: Motivo: {e}")

    return registros

