# Vous devez construire un organisateur de fichier à partir de ce dictionnaire.
# Le programme scannera un dossier dans lequel il y a des fichiers (text, pdf ...) et devra créer le dossier correspondant au clé du dictionnaire, si durant le scan on trouve des fichiers il faudra les déplacer dans le dossier correspondant.
# Exemple : dans mon dossier il y a un fichier .pdf, le programme doit créer le dossier PDF et déplacer le fichier à l'intérieur
import os
import shutil

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

chemin = os.path.join(os.getcwd(), 'organizer')
print(os.listdir(chemin))
#
# for element in os.listdir(chemin):
#     chemin_element = os.path.join(chemin, element)
#     if os.path.isfile(chemin_element):
#         _, extension = os.path.splitext(element)
#         for key, values in folder_dict.items():
#             if extension.strip().lower() in values:
#                 chemin_dossier = os.path.join(chemin, key)
#                 # if not os.path.isdir(chemin_dossier):
#                 #     os.mkdir(chemin_dossier)
#                 os.makedirs(chemin_dossier, exist_ok=True)
#                 shutil.move(chemin_element, chemin_dossier)
#
# for element in os.scandir(chemin):
#     # print(element.name, element.path,
#     #       element.is_dir(), element.is_file())
#     if element.is_file():
#         _, extension = os.path.splitext(element.name)
#         for key, values in folder_dict.items():
#             if extension.strip().lower() in values:
#                 chemin_dossier = os.path.join(chemin, key)
#                 os.makedirs(chemin_dossier, exist_ok=True)
#                 shutil.move(element.path, chemin_dossier)

for folder, subfolders, files in os.walk(chemin):
    print(folder, subfolders, files)
    for file in files:
        chemin_file = os.path.join(folder, file)
        _, extension = os.path.splitext(file)
        for key, values in folder_dict.items():
            if extension.strip().lower() in values:
                chemin_dossier = os.path.join(chemin, key)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_destination = os.path.join(chemin_dossier, file)
                if not os.path.isfile(chemin_destination):
                    shutil.move(chemin_file, chemin_dossier)