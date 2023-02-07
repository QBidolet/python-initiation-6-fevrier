# un tuple est un itérable immuable

# un tuple vide
mon_tuple = ()
print(mon_tuple, type(mon_tuple))

# un tuple un élément
mon_tuple = (99,)
print(mon_tuple, type(mon_tuple))
mon_tuple = 99, 100
print(mon_tuple, type(mon_tuple))


def retourner_deux_nombres(a, b):
    return 1, 2


nombre = retourner_deux_nombres(1, 2)

# un tuple avec plusieurs éléments
mon_tuple = 98, 99
mon_tuple = (98, 99)

# passer d'un tuple à un liste
mon_tuple = (1, 2, 3)
ma_liste = list(mon_tuple)
print(ma_liste)

# et inversement
mon_tuple = tuple(ma_liste)
print(mon_tuple)

