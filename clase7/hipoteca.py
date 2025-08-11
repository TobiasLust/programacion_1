'''
David solicitó un crédito a 30 años para comprar una vivienda, 
con una tasa fija nominal anual del 5%. Pidió $500000 al banco y 
acordó un pago mensual fijo de $2684,11.
El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:
'''


'''
Supongamos que David adelanta pagos extra de $1000/mes 
durante los primeros 12 meses de la hipoteca.

Modificá el programa para incorporar estos pagos extra y
 para que imprima el monto total pagado junto con la cantidad de meses requeridos.
'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
total_pagado = 0.0
meses_req = 0

while saldo > 0:
    meses_req += 1

    
    if meses_req >= pago_extra_mes_comienzo and meses_req <= pago_extra_mes_fin :
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra    
        total_pagado = total_pagado + pago_mensual + pago_extra
    elif meses_req == 310:
        saldo = saldo * (1+tasa/12)
        total_pagado = total_pagado + saldo
        saldo -= saldo
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

    print(f'{meses_req}. {round(total_pagado,2)}')
    

print(f'Total pagado: {round(total_pagado,2)}\nMeses: {meses_req}')