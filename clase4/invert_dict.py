precios = {"Pera": 490.1, "Lima": 23.45, "Naranja": 91.1, "Mandarina": 34.23}

print(precios.items())

list_precios = list(zip(precios.values(),precios.keys()))
print(list_precios)