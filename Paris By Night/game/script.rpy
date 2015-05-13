init python :
    from fonctions import *

# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")


# Le jeu commence ici
label start:



    python:
        langue_utilisee(_preferences.language)
    


    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pouvez le présenter au monde entier!"


    call introduction from _call_introduction


