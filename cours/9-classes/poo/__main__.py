from voiture import Voiture
from voiture_de_course import VoitureDeCourse

def main():
    ma_voiture = Voiture(couleur="noir", marque="Mercedes")
    ma_voiture_2 = Voiture()
    print(ma_voiture > ma_voiture_2)
    print(ma_voiture == ma_voiture_2)
    print(ma_voiture.__eq__(ma_voiture_2))
    voiture_de_course = VoitureDeCourse("noir", "Tesla", 320)
    print(voiture_de_course)


if __name__ == "__main__":
    main()
else:
    # faire autre chose
    pass