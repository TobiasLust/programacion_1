'''
Una pelota de goma es arrojada desde una altura de 100 metros y 
cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
Escribí un programa rebotes.py que 
imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.
'''
import sys

def rebotar(altura,rebotes):

    # altura pelota
    altura = altura

    # var del salto
    var_salto = 3/5


    # rebotes de la pelota
    count = 0

    while count < rebotes:
        altura =altura * var_salto
        
        count += 1

        print(f'Rebote {rebotes} alcanza una altura de: {altura:.2f} mts')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(f'Ingrese: {sys.argv[0]} altura:num rebotes:num')
    else:
        rebotar(int(sys.argv[1]),float(sys.argv[2])) 
     