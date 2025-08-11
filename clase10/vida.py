from datetime import datetime


def vida_en_segundos(fecha_nac):
    """
    Devuelve el tiempo de vida en segundos como float asumiendo
    que naciste a las 00:00hs
    La cadena fecha_nac debe ser en formato
    'dd/mm/AAAA'
    """
    try:
        fecha = datetime.strptime(fecha_nac, "%d/%m/%Y")
    except ValueError:
        print(f'No se pudo formatear {fecha_nac}\nel formato es dd/mm/AAAA ')
        return False
    hoy = datetime.now()

    tiempo_vida = hoy - fecha
    return round(float(tiempo_vida.total_seconds()),2)
