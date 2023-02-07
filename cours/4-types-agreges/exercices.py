"""
4.1 Créer une liste qui contient plus de 2 éléments. Ensuite, supprimer les deux derniers
éléments de la liste.

4.2 Créer un tuple avec plus de 5 éléments. Puis, afficher le troisième élément de celui-ci.
Peut-on afficher le troisième élément depuis la fin ?

4.3 Quelle est la différence entre un tuple et une liste ?

4.4 Prédire le resultat :
mon_tuple = (1, 2, 2, 3, 4, 4, 5)
mon_set = set(mon_tuple)
print("Le set est:")
print(mon_set)

4.5 Pouvez-vous déterminer si le code suivant génère une erreur ?
ma_liste=["rouge", "bleu"]
mon_set = set(ma_liste)
print("Le set est:")
print(mon_set)
mon_set.discard("vert")

4.6 Créer un dictionnaire et afficher son contenu.
Pouvez-vous afficher la valeur d'une clé particulière ?
"""

# 4.1
ma_liste = ["John", 12, 35, 45, True]
print("Contenu de la liste :")
print(ma_liste)

# Suppression des deux derniers éléments
del ma_liste[-2:]
print(ma_liste)

# 4.2
mon_tuple = ("John", 12, 35, True, 5.08)
print("Le tuple :")
print(mon_tuple)

# Le troisième élément
print(mon_tuple[2])
print(mon_tuple[-3])

# 4.3
# Les tuples sont immuables et les listes mutables.

# 4.4
# Les doublons sont supprimés et les éléments sont désordonnés.

# 4.5
# L'élément "vert" n'est pas présent dans le set.
# Avec remove vous allez générer l'erreur suivante :
# KeyError
# En renvanche, discard() ne génère pas d'errreur.
# discard() supprime l'élément que si celui-ci existe.

# 4.6
mon_dict = {
    "nom": "BIDOLET",
    "prenom": "Quentin"
}
print(mon_dict["prenom"])
