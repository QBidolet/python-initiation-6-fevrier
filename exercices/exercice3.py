"""
Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée.
Par exemple, si on l'appliquait à
la liste [32, 5, 12, 8, 3, 75, 2, 15],
ce programme devrait afficher : 75.
BONUS : Ne pas utiliser la fonction sort, ni max, ni min
"""

liste = [32, 5, 12, 8, 3, 75, 2, 15]

# version 1
if liste:
    maximum = liste[0]
    for i in range(len(liste)):
        if liste[i] > maximum:
            maximum = liste[i]
    print(maximum)
else:
    print("Veuillez rentrer une liste valide.")

# version 2
if liste:
    maximum = liste[0]
    for element in liste:
        if element > maximum:
            maximum = element
    print(maximum)