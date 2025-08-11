'''
Una pelota de goma es arrojada desde una altura de 100 metros y 
cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
Escribí un programa rebotes.py que 
imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.
'''

# altura pelota
ALTURA = 100

# var del salto
var_salto = 3/5


# rebotes de la pelota
rebotes = 0

while rebotes < 10:
    ALTURA = ALTURA * var_salto
    
    rebotes += 1

    print(f'Rebote {rebotes} alcanza una altura de: {ALTURA:.1f} mts')

