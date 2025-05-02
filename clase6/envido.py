import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ["oro", "copa", "espada", "basto"]
naipes = [(valor, palo) for valor in valores for palo in palos]


def crear_mano(naipes):
    mano = random.sample(naipes, k=3)
    return mano


def valor_envido(mano):
    valores = []
    max_envido = 0
    for valor, palo in mano:
        if valor in range(10, 13):
            valores.append((0, palo))
        else:
            valores.append((valor, palo))

    for i in range(len(valores)):
        for j in range(i + 1, len(valores)):
            valor1, palo1 = valores[i]
            valor2, palo2 = valores[j]

        if palo1 == palo2:
            suma = valor1 + valor2 + 20
            if suma > max_envido:
                max_envido = suma

    if max_envido == 0:
        max_envido = max(valor for valor, _ in valores)

    if max_envido in range(31, 34):
        return True
    return False


N = 10000

E = sum([valor_envido(crear_mano(naipes)) for i in range(N)])
prob = E / N
print(
    f"Observamos {N} manos de truco, de los cuales {E} tuvieron un envido entre 31 y 33."
)
print(
    f"Podemos estimar la probabilidad de que en una mano de truco aparezca un envido entre 31 y 33 {prob:.6f}."
)
