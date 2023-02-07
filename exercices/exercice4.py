"""
A partir de cette liste
["Jean", "Maximilien", "Brigitte", "Sonia"]
Coder un programme permettant de séparer
les prénoms, une liste avec ceux
ayant moins de 6 caractères (6 inclus)
et ceux ayant plus de 6 caractères.
"""

ma_liste = ["Jean", "Maximilien", "Brigitte", "Sonia"]
liste_supp_6 = []
liste_inf_ou_6 = []

for element in ma_liste:
    if len(element) > 6:
        liste_supp_6.append(element)
    else:
        liste_inf_ou_6.append(element)

print(f"Liste plus de 6 caractères : {' - '.join(liste_supp_6)}")
print(f"Liste à moins ou à 6 caractères : {liste_inf_ou_6}")

# Correction avec des compréhensions de liste
liste_sup_6 = [element for element in ma_liste if len(element) > 6]
print(liste_sup_6)

liste_avec_10_premier_nombre_pair_carre = [element ** 2 for element in range(0, 20) if element % 2 == 0]

ee = [element//2 if element % 2 == 0
      else element*3+1 for element in range(0, 20)]
print(ee)
