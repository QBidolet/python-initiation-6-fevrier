this_list = ["apple", "banana", "cherry"]
this_list = list(("apple", "banana", "cherry"))

# liste vide
this_list = []
this_list = list()

print(this_list)
print(type(this_list))

liste = ["cat", [10, 30, 36], 'mouse']
print(liste)

# afficher le premier élément
print(liste[0])
print(liste[1][1])

# -1 est le dernier élément, -2 l'avant dernier etc ...
print(liste[-2][-2])

print("#"*25)
# Ajouter dans une liste
liste = [1, 2, 3]
liste.append(4)
print(liste)

liste.insert(0, -99)
print(liste)

print(liste.count(-99))
print(len(liste))
liste.append(-99)
print(liste)
# liste.remove(50000)  # première occurrence uniquement
print(liste)

del liste[0]

resultat = liste.pop(0)
print(resultat)

liste = [1, 2, 3, 4]
# attribution
liste[0] = 12
print(liste)

# Copie
garage = ["Clio", "Peugeot", "Ferrari"]
garage_2 = garage
print(id(garage), id(garage_2))
garage[0] = "Volvo"
print(garage_2)

# Copy
garage_1 = ["Ferrari", "Volvo", "Peugeot"]
garage_2 = garage_1.copy()
print(id(garage_1), id(garage_2))
garage_1[0] = "Clio"
print(garage_1, garage_2)

# appartenance
if "Clio" in garage_1:
    print("Clio est dans le garage.")

for voiture in garage_1:
    print(voiture)

# trier
garage_2.sort(reverse=True)
print(garage_2)

# passer d'une liste à un string
ma_liste = ["oui", "non", "ok"]
print("/".join(ma_liste))

# passer d'un string à une liste
chaine = "oui:non:ok"
liste = chaine.split(":")
print(liste)


