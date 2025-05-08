import csv
f = open('../Data/camion.csv')

types = [str, int, float]

rows = csv.reader(f)
headers = next(rows)

row = next(rows)
print(row)

r = list(zip(types,row))

converted = [func(val) for func, val in zip(types, row)]


print(converted)

precios_dict = { name: func(val) for name, func, val in zip(headers, types, row) }
print(precios_dict)