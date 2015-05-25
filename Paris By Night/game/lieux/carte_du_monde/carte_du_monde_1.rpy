## Carte du monde

init python :
    from fonctions import *
    

screen demo_imagemap(nom_worldmap):
    $ lieux_disponibles = [
        (8, 200, "swimming", "Swimming", "lieux/carte_du_monde/nage.png", "lieux/carte_du_monde/nage_hover.png"),
        ]

    default tt = Tooltip("")

    python :
        langue_utilisee(_preferences.language)
        lieux_disponibles = carte_monde(lieux_disponibles, persistent.mods, nom_worldmap)

    imagemap:
        ground "lieux/carte_du_monde/fond_worlmap1.jpg"
        for xposition, yposition, actionn, txt, imagebase, imagehover in lieux_disponibles:
            imagebutton :
                idle imagebase 
                hover imagehover
                xpos xposition  
                ypos yposition
                action Return(actionn)
                hovered tt.Action((txt))

    fixed:
        text tt.value xalign 0.5 yalign 0.97 color "#3B3F40" bold 1 outlines [ (3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0) ]
        at my_transform


label worldmap_1 :
    call screen demo_imagemap('worldmap_1')

    # Call screen assignes the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.

    if _return == "swimming":

        avatar "You chose swimming."

        avatar "Swimming seems like a lot of fun, but I didn't bring my bathing suit with me."

    elif _return == "science":

        avatar "You chose science."

        avatar "I've heard that some schools have a competitive science team, but to me research is something that can't be rushed."

    elif _return == "art":

        avatar "You chose art."

        avatar "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    elif _return == "go home":

        avatar "You chose to go home."