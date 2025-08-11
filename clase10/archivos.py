import os
print(os.getcwd()) # dic actual

# os.mkdir crear
# os.chdir / os.chdir(..) cambiar al directorio relativo
# os.rmdir borra el dir debe estar vacio
# os.listdir list de archivos y dir
# os.rename cambia nombre

#directorio = os.path.join('/home', 'usuario', 'ejercicios_python')
#os.chdir(directorio)

import shutil 
#shutil.rmtree('carpeta')

for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))



# Importamos módulos necesarios
import os                 # Para acceder a funciones del sistema operativo
import datetime           # Para crear y manipular fechas y horas
import time               # Para convertir timestamps en fechas legibles

# Ruta relativa del archivo al que vamos a modificar las fechas
camino = '../Clase06/rebotes.py'

# Obtenemos las estadísticas actuales del archivo (como tamaño, fecha de acceso y modificación)
stats_archivo = os.stat(camino)

# Mostramos la fecha de último acceso en formato legible
print("Fecha de acceso original:", time.ctime(stats_archivo.st_atime))
# Referencia: https://docs.python.org/3/library/os.html#os.stat
# Referencia: https://docs.python.org/3/library/time.html#time.ctime

# Creamos dos fechas personalizadas con el módulo datetime
# Una para el nuevo acceso y otra para la nueva modificación
fecha_acceso = datetime.datetime(year=2017, month=9, day=21, hour=19, minute=51, second=0)
fecha_modifi = datetime.datetime(year=2012, month=9, day=24, hour=12, minute=9, second=24)
# Referencia: https://docs.python.org/3/library/datetime.html#datetime.datetime

# Convertimos esas fechas en timestamps (segundos desde el 1/1/1970)
ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
# Referencia: https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp

# Modificamos la fecha de acceso y de modificación del archivo
os.utime(camino, (ts_acceso, ts_modifi))
# Referencia: https://docs.python.org/3/library/os.html#os.utime

# Mostramos la nueva fecha de último acceso
print("Nueva fecha de acceso:", time.ctime(stats_archivo.st_atime))

# También mostramos la nueva fecha de última modificación
print("Nueva fecha de modificación:", time.ctime(stats_archivo.st_mtime))
