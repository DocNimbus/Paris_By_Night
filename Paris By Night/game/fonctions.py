from variables_globales import *

def dictionnaire(persistent): #Liste des mods dispo, ce qu'ils proposent et si il sont activés ou non
# Les imports 
    import os
    import renpy
    import xml.etree.ElementTree as elementtree

    dictionnaire_mods = {}
    nb_de_mods = 0
    for root, dirs, files in os.walk(renpy.config.gamedir  + '/mods'):
        path = root.split('/')
        for file in files:
            if file == ('manifest.xml'):         
                nb_de_mods =  nb_de_mods + 1
                tree = elementtree.parse(root + '/manifest.xml')
                namemod = tree.findtext('name', default='Non disponible')
                if namemod != 'Non disponible': # Si pas de nom, on abandonne      
                    author_mod = tree.findtext('author', default='Non disponible')
                    version_mod = tree.findtext('version_mod', default='Non disponible')
                    place_mod = tree.findtext('places', default=0)
                    character_mod = tree.findtext('character', default=0)
                    discussion_mod = tree.findtext('discussion', default=0)
                    enquete_mod = tree.findtext('enquete', default=0)
                    enquete_alea_mod = tree.findtext('enquete_alea', default=0)
                    objets_mod = tree.findtext('objets', default=0)
                    chemin_mod = str(os.path.split(root)[1:])[3:-3]
                    mod_actif = persistent[namemod]
                    liste_var_mods = range(len(liste_dico_mod))
                    i = 0
                    for i in range(0,len(liste_dico_mod)) :
                        liste_var_mods[i] = eval(liste_dico_mod[i])
                        i = i+1
                    dictionnaire_mods[nb_de_mods] = liste_var_mods
    
    return dictionnaire_mods

def carte_monde(lieux_disponibles, persistent, nom_worldmap): #Les déjà existantes, + parametre persistent pour savoir ce qui est vraiment activé + nom de la carte
# Les imports 
    import os
    import renpy
    import xml.etree.ElementTree as elementtree
    
# On met à jour le référentiel
    dictionnaire_mods = dictionnaire(persistent)
    
# On lance la machine
    for key, mods in dictionnaire_mods.items() :       
        if mods[liste_dico_mod.index('mod_actif')] == '1' and mods[liste_dico_mod.index('place_mod')] == '1':
            chemin_mod = str(mods[liste_dico_mod.index('chemin_mod')])
            for root, dirs, files in os.walk(renpy.config.gamedir + '/mods/' + chemin_mod + '/places'):
                path = root.split('/')
                for file in files:
                    if file == ('places.xml'): # Le bon fichier existe ?
                        tree = elementtree.parse(root + '/places.xml')
                        if tree.findtext(nom_worldmap, default='Non disponible') != 'Non disponible': # Si pas le bon tag, on abandonne
                            a = 1
                            for a in [1,len(list(tree.find(nom_worldmap)))] :
                                chemin = str(nom_worldmap) + "/" + str(list(tree.find(nom_worldmap))[a-1])[10:-14].replace("'","")
                                if tree.findtext(chemin + '/condition', default='Non disponible') == 'Non disponible' or \
                                eval(tree.findtext(chemin + '/condition', default='Non disponible')):  # si il n'y a pas de condition particulière (ci-dessus) ou si la condition est vérifiée on pousuit
                                    lieux_disponibles.append(( \
                                        eval(tree.findtext(chemin + '/xposition', default=1280)),                           # position par rapport au bord gauche de l'écran                                                                       
                                        eval(tree.findtext(chemin + '/yposition', default=1280)),                           # position par rapport au haut de l'écran
                                        eval(tree.findtext(chemin + '/exit', default="Nope")),                              # lieu de sortie
                                        eval(tree.findtext(chemin + '/name', default="Nope")),                              # Nom de la sortie
                                        "mods/" + chemin_mod + tree.findtext(chemin + '/idle', default=""),                 # Chemin vers icône idle
                                        "mods/" + chemin_mod + tree.findtext(chemin + '/hover', default="")))               # Chemin vers icône quand le curseur est dessus                                 
                                a = a+2

    return lieux_disponibles
    