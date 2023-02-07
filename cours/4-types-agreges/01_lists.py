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
liste.remove(50000)  # première occurrence uniquement
print(liste)

del liste[0]