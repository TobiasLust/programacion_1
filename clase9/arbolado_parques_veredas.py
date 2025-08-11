import pandas as pd
import matplotlib.pyplot as plt

df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv') # 'altura_tot', 'diametro' y 'nombre_cie'
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv') # 'altura_arbol', 'diametro_altura_pecho' y 'nombre_cientifico'

cols_parques = ['nombre_cie','altura_tot','diametro']
cols_veredas = ['nombre_cientifico','altura_arbol', 'diametro_altura_pecho']

df_tipas_parques = df_parques[df_parques['nombre_cie'].str.contains('Tipuana')][cols_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].str.contains('Tipuana')][cols_veredas].copy()

df_tipas_veredas['nombre_cientifico'] = df_tipas_veredas['nombre_cientifico'].str.title()

df_tipas_parques.rename(columns={cols_parques[0]: cols_veredas[0],cols_parques[1]: cols_veredas[1],cols_parques[2]: cols_veredas[2]}, inplace=True)

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'


df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')
plt.show()
df_tipas.boxplot('altura_arbol', by = 'ambiente')
plt.show()