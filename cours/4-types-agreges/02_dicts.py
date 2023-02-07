mon_dict = {
    "nom": "BIDOLET",
    "prenom": "Quentin",
    "age": 28
}

print(mon_dict, type(mon_dict))

# accès
print(mon_dict["nom"])

# modifier
mon_dict["age"] = 55
print(mon_dict)

print('#'*25)
print(type(mon_dict.keys()))

if 'prenom' in mon_dict.keys():
    print('oui')

# présence d'une valeur
if "Quentin" in mon_dict.values():
    print("Quentin est présent dans le dictionnaire")

# présence d'un item
if ('prenom', "Quentin") in mon_dict.items():
    print("L'item est présent")

users = {
    "user_1": {
        "name": "Quentin",
        "age": 29
    }
}

print(users.get("user_1").get("name"))
print(users["user_1"]["name"])
