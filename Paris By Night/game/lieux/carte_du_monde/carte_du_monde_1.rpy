## Carte du monde


screen demo_imagemap:

    $ tutorials = [
        (8, 200, 78, 78, "swimming", "Swimming"),
        (204, 50, 78, 78, "science", "Science"),
        (452, 79, 78, 78, "art", "Art"),
        ]

    for key, (chemin_mod, namemod, version_mod, version_game_mod, place_mod, character_mod, discussion_mod, enquete_mod, enquete_alea_mod, objets_mod, actif) in dictionnaire_mods.items() : 
        if actif == '1' and place_mod == '1':
            for root, dirs, files in os.walk(config.gamedir + '/mods/' + str(chemin_mod) + '/places'):
                $ path = root.split('/')
                for file in files:
                    if file == ('places.xml'):
                        $ tree = elementtree.parse(root + '/places.xml')
                        $ worldmap = tree.findtext('worldmap', default='Non disponible')
                        if worldmap != 'Non disponible': # Si pas de nom, on abandonne
                            $ bob = (eval(tree.findtext('worldmap/element1/xposition', default=0)), 316, 78, 78, "go home", "Go Home")
                            $ tutorials.append(bob) 

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