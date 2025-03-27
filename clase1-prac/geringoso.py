'''
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
'''

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    match c.lower():
        case 'a':
            capadepenapa += c + 'pa'
            continue
        case 'e':
            capadepenapa += c + 'pe'
            continue
        case 'i':
            capadepenapa += c + 'pi'
            continue
        case 'o':
            capadepenapa += c + 'po'
            continue
        case 'u':
            capadepenapa += c + 'pu'
            continue
        case _:
            capadepenapa += c

print(capadepenapa)

