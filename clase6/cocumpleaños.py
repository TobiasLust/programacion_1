import random

AÑO = {
    "ene": 31,
    "feb": 28,
    "mar": 31,
    "abr": 30,
    "mayo": 31,
    "jun": 30,
    "jul": 31,
    "ago": 31,
    "sept": 30,
    "oct": 31,
    "nov": 30,
    "dic": 31,
}


def crear_cumpleaños():
    cumpleaños = []
    for _ in range(30):
        mes = random.choice(list(AÑO.keys()))
        dia = random.randint(1, AÑO[mes])
        cumpleaños.append((mes, dia))

    return cumpleaños


def cocumpleaños(cumpleaños):
    return len(set(cumpleaños)) < len(cumpleaños)


N = 10000000

T = sum([cocumpleaños(crear_cumpleaños()) for i in range(N)])
prob = T / N
print(
    f"Observamos {N} grupos de 30 alumnos, de los cuales {T} tuvieron un cocumpleaños."
)
print(
    f"Podemos estimar la probabilidad de que en un grupo de 30 personas aparezca un cocumpleaños mediante {prob:.6f}."
)
