# copier un fichier dans un dossier
import os
import shutil

src = os.path.join(os.getcwd(), "texte.txt")
dst = os.path.join(os.getcwd(), "data", "texte2.txt")
# Attention, le répertoire destination doit exister
os.makedirs("data", exist_ok=True)
# os.mkdir("data")

shutil.copy(src, dst)

# faire une sauvegarde complète d'un dossier
src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_backup")
# shutil.copytree(src, dst)
# shutil.make_archive("archive", "zip", "data")

# suppression récursive, avec TOUT le contenu
# shutil.rmtree(dst)

# suppression récursive des dossiers
# s'il n'y a pas de fichier
# os.removedirs(dst)

# déplacer
shutil.move(src, dst)
# pour renommer, changer dans le chemin
# de destination le nom du fichier