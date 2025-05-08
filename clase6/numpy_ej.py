import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


print(a[2, 3], a[2][3])

b = np.empty(3)
print(b, np.arange(4))

# ej 6.7

impares = np.arange(1, 20, 2)

impares2 = np.linspace(1, 19, num=10, dtype=np.int64)
print(impares, impares2)

# np.concatenate((a, b))
np.sort(impares)

# ndim : cantidad de dimensiones   shape: tupla cant e en cada eje ejemplo 2 filas y 3 colum (2,3) size

array_ej = np.array(
    [[[0,1,2,3],[4,5,6,7]],[[0,1,2,3],[4,5,6,7]],[[0,1,2,3],[4,5,6,7]]]
)

print(array_ej.ndim,array_ej.shape,array_ej.size)

#cambiar fomra

a_ej = np.arange(6)
print(a_ej)
b_ej = a_ej.reshape(3,2)
print(b_ej)


#indices y filtrados

data = np.array([4,5,6])
print(data[0:2],data[-2:])


a_sinfilt = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

a_filt = a_sinfilt[a<5]

print(a_sinfilt,a_filt,id(a_sinfilt),id(a_filt))

indices = np.nonzero(a<5)
print(indices) #primero q fila y dsp q columna

lista_cord = list(zip(indices[0], indices[1]))
print(lista_cord)

 
data1 = np.array([[1, 2], [3, 4], [5, 6]])

print(data[0,1]) # accedo fila 0 columna 1
print(data[1:3])# me quedo con la fila 1 y la 2
print(data[0:2,0]) # de las fila 0 y 1 me quedo con la columna 0

