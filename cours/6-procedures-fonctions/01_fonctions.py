from typing import Tuple


def ma_function(a: int, b: int) -> Tuple[str, int, int]:
    """
    Super fonction qui retourne a et b.
    :param a: un entier.
    :param b: un entier.
    :return: a et b.
    """
    return a, b


resultat = ma_function(12, 24)
print(resultat)


def somme(a, b):
    return a + b


print(somme(1, 2))
print(somme(1, somme(2, 3)))


# Faire une fonction qui additionne tous les nombres
# d'une liste.
def somme(ma_liste):
    resultat = 0
    for element in ma_liste:
        resultat += element
    return resultat


ma_liste = [1, 2, 3]
print(id(ma_liste))
print(somme(ma_liste))
print(ma_liste)


# Somme avec passage de paramètres illimités.

def somme(*args):
    print(args)
    resultat = 0
    for element in args:
        resultat += element
    return resultat


ma_liste = [1, 2, 3, 4, 5, 6]
print(somme(ma_liste))
