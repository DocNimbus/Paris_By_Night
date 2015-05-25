
init:
    image black = "#000000"
#    image bg_classe_day = "histoire/prologue/episode_1/lieux/place_classroom_evening.png"
#    $ dico_portraits = ('histoire/prologue/episode_1/portraits/Bertrand_Ouellet/Bertrand_Ouellet_soiree_neutral.png', 'histoire/prologue/episode_1/portraits/Bertrand_Ouellet/Bertrand_Ouellet_normal_neural.png')

init python :
    from fonctions import *
  #  renpy.image(('avatar','etudiant_normal', 'angry'), 'portraits/avatar/etudiant_normal/angry.png')
  #  renpy.image(('avatar','etudiant_normal', 'neutral'), 'portraits/avatar/etudiant_normal/neutral.png')

    define_images('histoire/prologue/episode_1/portraits')


# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.

    


# Pour créer automatiquement une liste des portraits :
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=27844

label prologue_episode_1_script_1:
#    $ define_characters("histoire/prologue/episode_/portraits/", 1, False)
    define avatar = DynamicCharacter("name_avatar")
    define Bertrand_Ouellet = Character('Bertrand', color="66CC00")
    define Gregoire_Carriere = DynamicCharacter('Gregoire_Carriere', color="#EB2F2F")
    define Florence_Despins = Character('Florence', color="#B29138")
    define Nadine_Lussier = Character('Nadine', color="#A0A0A0")
    define Emilie = Character('Emilie', color="#3399FF")
       
    scene black

    python:
        langue_utilisee(_preferences.language)

    
    $ name_avatar = ''
    $ Gregoire_Carriere = DynamicCharacter('q', color="#EB2F2F")
    $ q = '(voix masculine)'
 #   $ Gregoire_Carriere = '(voix masculine)'

    Gregoire_Carriere "{size=-10}Hey{/size}"
    Gregoire_Carriere "Hey"
    Gregoire_Carriere "{size=+10}Hey !{/size}"

menu:
    "Que voulez-vous faire ?"

    "Ouvrir les yeux.":
        jump after_menu

    "Laisser vos paupières closes.":
        "Vous vous dite que quelques minutes de repos supplémentaires ne vous feront pas de mal."

        Gregoire_Carriere "Putain, mec, t'abuses, réveille toi rapidement ou tu vraiment te faire engueuler."

        menu:
            "Ouvrir les yeux.":
                jump after_menu


#     "Genuflect.":
#         jump after_menu

label after_menu:

    $ q = 'Grégoire'
    
    image bg_classe_day = "histoire/prologue/episode_1/lieux/place_classroom_evening.png"
    scene bg_classe_day
#    image avatar etudiant_normal angry = 'histoire/prologue/episode_1/portraits/avatar/etudiant_normal/angry.png'
#    show avatar etudiant_normal angry
    show avatar etudiant_normal happy

    Gregoire_Carriere "Mec, j'ai cru que tu pionçais encore !"

    avatar "Là, on affiche la worldmap"

    call worldmap_1 # from _call_worldmap