# set = ensemble désordonnée et sans doublons

heros = {
    "batman",
    "superman"
}

print(heros, type(heros))

heros.add("ant-man")
heros.add("ant-man")
print(heros)

heros.update(["captain-america", "black widow"])
print(heros)

heros.remove("batman")
print(heros)

# in
for hero in heros:
    print(hero)

if "superman" in heros:
    print("Superman est présent.")

# conversion
ma_liste = [1, 2, 3]
mon_set = set(ma_liste)
print(mon_set)

