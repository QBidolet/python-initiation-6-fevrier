from typing import Tuple


def ma_function(a: int, b: int) -> Tuple[int, int]:
    """
    Super fonction qui retourne a et b.
    :param a: un entier.
    :param b: un entier.
    :return: a et b.
    """
    return a, b


a, b = ma_function(12, 24)
print(a, b)


# a, b = [1, 2]
# print(a, b)

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
print(somme(1, 2))


# kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(a=1, b=2, c=3)

print("#" * 25)


def ma_fonction(chiffre, nombre=0, mot="Hello", *args, **kwargs):
    print(chiffre, nombre, mot, args, kwargs, sep="\n")


ma_fonction(9)

# variables globales
print("#" * 25)


def ma_fonction():
    global variable
    variable = 2
    print(f"Valeur de variable : {variable}")


ma_fonction()
print(f"Valeur de variable : {variable}")


# fonctions anonymes
def double(a):
    return a * 2


ma_liste = [1, 2, 3, 4]
nouvelle_liste = []
for nombre in ma_liste:
    nouvelle_liste.append(double(nombre))
print(nouvelle_liste)

# map : permet d'appliquer une transformation
# à tous les éléments d'un itérable

mon_map = map(double, ma_liste)
print(list(mon_map))

# définition d'une fonction anonyme
mon_map = map(lambda x: x * 2, ma_liste)
print(list(mon_map))

# liste en compréhension
nouvelle_liste = [double(element) for element in ma_liste]

# filter
print("#" * 25)
ma_liste = [6, 7, 8, 9]
print(ma_liste)
nouvelle_liste = filter(lambda a: a % 2 == 0, ma_liste)
print(list(nouvelle_liste))


# closure
def outer_function(x):
    def inner_function(y):
        return x + y

    def soustraction(y):
        return x - y

    return inner_function, soustraction


addition, soustraction = outer_function(10)
print(addition(5))


# fonctions génératrices
def range(n):
    compteur = 1
    while compteur <= n:
        yield compteur
        compteur += 1

generatrice = range(5)
print('#'*25)
print('#'*25)
for i in generatrice:
    print(i)
print('#'*25)
for i in generatrice:
    print(i)
