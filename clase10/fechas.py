import datetime

ahora = datetime.datetime.now() # fecha y hora del momento
datetime.date.today() # fecha
a = datetime.datetime(2020,9,21,12,50)

# formatear una hora
b = datetime.datetime.now().strftime('Son las %H, %M, %S segundos')

cadena = '21 september, 2021'
objeto = datetime.datetime.strptime(cadena,'%d %B, %Y')

#atributos clase datetime
ahora.year
ahora.month

# metodos
ahora.isocalendar() # año , numro semana , numero dia de esa semana
ahora.timestamp() # numeros de segs transcurridos desde el 1 de enero 1970

# time deltas

parcial_i = datetime.datetime(2020,9,16,14)
parcial_f = datetime.datetime(2020,9,16,15,30)

duracion = parcial_f - parcial_i
duracion.total_seconds()

from datetime import date

d = date(2019,4,13)
print(d)

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday())

licencia = datetime.datetime(2020,9,26)

