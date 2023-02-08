import gzip
import zlib


# Zlib
# On compresse que des fichiers binaires
original_data = open("texte.txt", "rb").read()
# niveau de compression va de 1 à 9, 9 était le plus compressé
compressed_data = zlib.compress(original_data, 2)

file = open("texte.gz", "wb")
file.write(compressed_data)
file.close()

compressed_data = open("texte.gz", "rb").read()
# décompresser
decompressed_data = zlib.decompress(compressed_data)
print(decompressed_data)


# Alternative : Gzip
f = gzip.open("texte.gz", "wt")
f.write("Hello")
f.close()

f = gzip.open("texte.gz")
print(f.read())
f.close()
