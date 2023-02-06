# nom de variable utilise le snake_case
# TOUS alphabets sauf -, @ ! ? \ / #
# un nom de variable ne doit pas commencer par
# un chiffre.

ma_boite = 42
ma_boite_2 = ma_boite
print(id(ma_boite), id(ma_boite_2))

ma_boite = 6
print(id(ma_boite), id(ma_boite_2))
print(ma_boite_2)

# nom de variables valides
# a, a_1, a_b_c_______95, _abc, _1a

# nom de variables invalides
# 1a, 1, 1_