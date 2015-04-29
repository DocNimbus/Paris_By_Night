## Carte du monde

init python:

    bob = (602, 316, 78, 78, "go home", "Go Home")

    tutorials = [
        (8, 200, 78, 78, "swimming", "Swimming"),
        (204, 50, 78, 78, "science", "Science"),
        (452, 79, 78, 78, "art", "Art"),
        bob ,        
        ]
    
screen demo_imagemap:
    imagemap:
        auto "lieux/carte_du_monde/imagemap_%s.jpg"
        for x, y, xwidth, yheight, actionn, alternaite in tutorials:
            hotspot (x, y, xwidth, yheight) action Return(actionn) alt alternaite
  

label worldmap_1 :
    call screen demo_imagemap

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