"""
Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
 Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso
 (como en el Ejercicio 1.18).
 Probá tu función para la lista ['banana', 'manzana', 'mandarina'].
"""


def geringoso(word):
    new_word = ""
    for c in word:
        match c.lower():
            case "a":
                new_word += c + "pa"
                continue
            case "e":
                new_word += c + "pe"
                continue
            case "i":
                new_word += c + "pi"
                continue
            case "o":
                new_word += c + "po"
                continue
            case "u":
                new_word += c + "pu"
                continue
            case _:
                new_word += c
    return new_word


def main():
    words = ["banana", "manzana", "mandarina"]
    dict_geringoso = {}

    for word in words:
        dict_geringoso[word] = geringoso(word)

    print(f"Diccionario Geringoso:\n")
    for k,v in dict_geringoso.items():
        print(f"{k}: {v}")


main()
