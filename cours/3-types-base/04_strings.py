# escape avec \
ma_phrase = "J'ai mon masque."

ma_phrase = 'J\'ai mon masque.'

# multiligne
ma_phrase = """J'ai mon masque
et je suis content.
"""

# retour chariot
ma_phrase = "J'ai mon masque\net je suis content."

# Combiner avec +
prenom = "Quentin"
nom = "BIDOLET"

# version 1
print("Je m'appelle " + prenom + " " + nom + ".")

# version 2
print("Je m'appelle %s %s." % (prenom, nom))

# version 3
print("Je m'appelle {0} {1}.".format(prenom, nom))

# version pythonic
print(f"Je m'appelle {prenom} {nom}.")

# duplique
print('*'*25)

# extraire avec []
alphabet = "abcdefg"
print(alphabet[0])

# [ start : end : step ]
# [:] : prendre toute la chaine.
print(alphabet[:])
# [start:] : démarre à l'offset jusqu'à la fin.
print(alphabet[2:])
# [:end]
print(alphabet[:2])
# [start:end] : offset à offset
print(alphabet[2:4])

print(alphabet[::-1])