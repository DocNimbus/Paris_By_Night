## Carte du monde

init python :
    from fonctions import *
    

screen demo_imagemap(nom_worldmap):
    $ lieux_disponibles = [
        (8, 200, "swimming", "Swimming", "lieux/carte_du_monde/nage.png", "lieux/carte_du_monde/nage_hover.png"),
        ]

    python :
        lieux_disponibles = carte_monde(lieux_disponibles, persistent.mods, nom_worldmap)

    imagemap:
        ground "lieux/carte_du_monde/fond_worlmap1.jpg"
        for xposition, yposition, actionn, alternaite, imagebase, imagehover in lieux_disponibles:
            imagebutton :
                idle imagebase 
                hover imagehover
                xpos xposition  
                ypos yposition
                action Return(actionn) # alt alternaite idle imagebase hover imagehover left_padding x top_padding y


label worldmap_1 :
    call screen demo_imagemap('worldmap_1')

    # Call screen assignes the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.

    if _return == "swimming":

        e "You chose swimming."

        e "Swimming seems like a lot of fun, but I didn't bring my bathing suit with me."

    elif _return == "science":

        e "You chose science."

        e "I've heard that some schools have a competitive science team, but to me research is something that can't be rushed."

    elif _return == "art":

        e "You chose art."

        e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    elif _return == "go home":

        e "You chose to go home."