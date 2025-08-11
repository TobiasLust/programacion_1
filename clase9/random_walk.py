import numpy as np
import matplotlib.pyplot as plt

# Función que genera una caminata aleatoria
def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()

# Cantidad de pasos por caminata
N = 100000

# Generamos 12 trayectorias
trayectorias = [randomwalk(N) for _ in range(12)]

# Calculamos las distancias máximas al origen para cada caminata
distancias_max = [np.max(np.abs(trayectoria)) for trayectoria in trayectorias]

# Encontramos el índice de la más alejada y la más cercana
indice_mas_alejada = np.argmax(distancias_max)
indice_menos_alejada = np.argmin(distancias_max)

# Configuración de subplots
fig = plt.figure(figsize=(12, 8))

# Subplot superior: las 12 trayectorias
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
for trayectoria in trayectorias:
    ax1.plot(trayectoria)
ax1.set_title("Caminatas Aleatorias (12 trayectorias)")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Distancia al origen")

# Subplot inferior izquierdo: la más alejada
ax2 = plt.subplot2grid((2, 2), (1, 0))
ax2.plot(trayectorias[indice_mas_alejada], color="red")
ax2.set_title("Trayectoria más alejada del origen")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Distancia al origen")

# Subplot inferior derecho: la más cercana
ax3 = plt.subplot2grid((2, 2), (1, 1))
ax3.plot(trayectorias[indice_menos_alejada], color="green")
ax3.set_title("Trayectoria menos alejada del origen")
ax3.set_xlabel("Tiempo")
ax3.set_ylabel("Distancia al origen")

plt.tight_layout()
plt.show()
