"""
Vous devez écrire un programme qui demande à l'utilisateur de saisir une vitesse en mile /heure
 et vous devez afficher cette vitesse en km/h et m/s
Vous devez également réinviter votre utilisateur à saisir une valeur une fois
la conversion terminé et boucler de cette façon
Indication pour la conversion : pour passer des miles/heure au mètre par seconde il faut diviser par 2.237
Indication pour la conversion : pour passer des miles/heure au km par heure il faut multiplier par 1.609
"""

liste_continuer = ["oui", "yes", "Oui", "Yes"]
continuer = "oui"
while continuer in liste_continuer:
    print("Saisir une vitesse en miles/heure.")
    saisie = float(input())
    m_s = saisie / 2.237
    km_h = saisie * 1.609
    print(f"{km_h} km/h, {m_s} ms\n")
    continuer = input("Voulez-vous continuer ?")