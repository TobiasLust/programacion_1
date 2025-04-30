#a = [1, 2, 3, 4, 5]
#b = [2*x for x in a]




nombres = ['Edmundo','Carlos']
nombre_l = [nombre.lower() for nombre in nombres]
print(nombre_l)

#[<expresión> for <variable> in <secuencia>].

a = [1, -5, 4, 2, -2, 10]
b = [x*2 for x in a if x > 0]
print(b)