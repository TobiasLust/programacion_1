"""
Escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada fruta (o verdura)
y lo imprima en pantalla.
Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.
"""

import csv

PRICES_LIST = '../Data/precios.csv'


def search_price(product):
    try:
        with open(PRICES_LIST) as file:
            product_list = csv.DictReader(file)

            # Recorre la lista buscando el producto, si lo encuentra retorna el dict del producto
            for p in product_list:
                if product in p["producto"]:
                    return p
        return None
    except FileNotFoundError:
        print(f"{PRICES_LIST} no existe")


def main():

    user_input = (
        input("Ingrese fruta/verdura para averiguar su precio x cajon: ")
        .strip()
        .capitalize()
    )
    product = search_price(user_input)
    if product:
        print(f"\nEl precio de un cajón de {user_input} es: {product['precio']}")
    else:
        print(f"{user_input} no figura en el listado de precios")


main()
