class Voiture:
    nombre_roue = 4

    def __init__(self, couleur="Verte", marque="Tesla"):
        self.couleur = couleur
        self.marque = marque

    def klaxonner(self):
        print("tut tut")

    def repeindre(self, couleur):
        self.couleur = couleur

    def afficher(self):
        return f"Couleur: {self.couleur} | Marque: {self.marque}"

    def __str__(self):
        return f"Couleur: {self.couleur} | Marque: {self.marque}"

    def __eq__(self, other):
        return self.couleur == other.couleur and self.marque == other.marque

    def __gt__(self, other):
        return len(self.marque) > len(other.marque)

    def __lt__(self, other):
        return len(self.marque) < len(other.marque)

    def __len__(self):
        return len(self.color)
