nom = "Quentin"
age = 28

# if
if nom == "Julien":
    print("Bonjour Julien.")
elif age == 70:
    print("Bonjour Monsieur.")
else:
    print("Bonjour.")

# boucles
# for

for caractere in nom:
    print(caractere)

print("#"*25)
for indice, caractere in enumerate(nom):
    print(indice, end=" ")
    print(caractere)

# range
for element in range(0, 20, 5):
    print(element)

for element in range(50):
    print(element)

# while
print("#"*25)
i = 0
while i < 10:
    print(i)
    if i != 0:
        # continue
        # break
        print(i)
    i += 1