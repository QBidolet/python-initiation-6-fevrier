from voiture import Voiture


class VoitureDeCourse(Voiture):
    def __init__(self, couleur, marque, vitesse):
        super().__init__(couleur, marque)
        self.vitesse = vitesse

    def __str__(self):
        return f"Je suis une voiture de {self.marque}" \
               f"de couleur {self.couleur}" \
               f"de vitesse {self.vitesse}"
