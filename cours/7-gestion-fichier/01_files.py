fichier = open('mon_fichier.txt', 'w')
fichier.write("Bonjour")
fruits = ["banane", "kiwi"]
fruits = map(lambda x: "\n" + x + "\n", fruits)
fichier.writelines(fruits)
fichier.close()

# Tout ce qui s'ouvre se ferme.

fichier = open('mon_fichier.txt', "r")
# print(fichier.read())
# print(fichier.readlines())
# print(fichier.read(2))
# print(fichier.readline())
print(fichier.read(2))
print(fichier.read())
fichier.seek(0)
print(fichier.read(2))
print(fichier.readline())
fichier.close()

with open('mon_fichier.txt', "a") as fichier:
    fichier.write("Fin programme")
    # fermeture automatique quand on sort du bloc
    with open('mon_fichier.txt', "a") as fichier:
        fichier.write("Fin programme")

print("Fin du programme, nous n'avons pas besoin"
      " de fermer le fichier.")
