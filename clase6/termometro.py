import random
import numpy as np

N = 999


def medir_temp(n):
    temp = 37.5
    mediciones = np.repeat(temp, n)
    for i in range(n):
        error = random.normalvariate(0, 0.2)
        mediciones[i] = round(temp + error, 1)

    np.save("../Data/temperaturas", mediciones)
    return np.sort(mediciones)


def resumen_temp(mediciones):
    temp_min = np.min(mediciones)
    temp_max = np.max(mediciones)
    temp_prom = round(np.mean(mediciones),1)
    temp_median = np.median(mediciones)
    q1 = mediciones[(mediciones.size // 4)]
    q3 = mediciones[(3 * (mediciones.size // 4))]
    
    return (temp_min, temp_max, temp_prom, temp_median, q1, q3)



resumen = resumen_temp(medir_temp(N))
print(f'''
Resumen de un total de {N} temperaturas con un desvio estandar de 0.2:
T min: {resumen[0]}
T max: {resumen[1]}
T promedio: {resumen[2]}
T mediana: {resumen[3]}
Primer quartil: {resumen[4]}
Tercer quartil: {resumen[5]}''')
