import random

N = 11


def medir_temp(n):
    temp = 37.5
    mediciones = []
    for _ in range(n):
        error = random.normalvariate(0, 0.2)
        mediciones.append(round(error + temp,1))
    return mediciones

def resumen_temp(n):
    n.sort()
    temp_min = min(n)
    temp_max = max(n)
    temp_prom = round(sum(n) / len(n), 1)
    q1 = n[(len(n)//4)]
    q3 = n[3*(len(n)//4)]
    
    if len(n) % 2 == 0:
        valor1 = len(n) // 2
        valor2 = valor1 - 1
        temp_median = (n[valor1] + n[valor2]) / 2
    else:
        temp_median = n[len(n) // 2]
    
    return (temp_min, temp_max, temp_prom, temp_median,q1,q3)

print(resumen_temp(medir_temp(N)))

