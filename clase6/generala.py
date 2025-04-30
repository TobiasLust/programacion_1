import random

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    
    return tirada

def es_generala(tirada):
    num = tirada[0]
    tirada_2 = tirada[1:]

    for dado in tirada_2:
        if dado != num:
            return False
    
    return True


N = 1000000

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

