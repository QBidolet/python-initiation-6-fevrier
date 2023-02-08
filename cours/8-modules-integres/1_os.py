import datetime
import os

# Sélectionner un chemin
chemin = os.path.join(os.getcwd(), "texte.txt")
print(chemin)

print(os.path.isfile(chemin))

# with open("texte.txt", "w") as fichier:
#     fichier.write("Hello")

# métadata
timestamp = os.path.getmtime("texte.txt")
derniere_modification = datetime.datetime.fromtimestamp(timestamp)
print(derniere_modification)

temps_ecoule = datetime.datetime.now() - derniere_modification
print(temps_ecoule.total_seconds())