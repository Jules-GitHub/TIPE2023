from PIL import Image
from numpy import asarray

# Chargement de l'image
image = Image.open(f"paris.png")
image = image.convert("RGB")
print(image.mode)
print(image.size)

# conversion en array numpy pour pouvoir traiter les données
data = asarray(image)

# conversion vers un fichier texte
with open(f"plan2.txt", "w") as fichier:
    height, width = image.size
    for k in range(width):
        for j in range(height):
            somme = 0   # Pour chaque donnée, on écrit dans le fichier l'entier correspondant
            for info in data[k][j]:
                somme *= 256
                somme += info
            fichier.write("0" if somme >= 0xeeeeee else "1")
        fichier.write(f"\n")