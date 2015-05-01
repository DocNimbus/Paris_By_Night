init -1 python:
    nb_de_mods = 0
    dictionnaire_mods = {}
    if not persistent.mods:
        persistent.mods = {}

# Des mods  sont-ils disponibles ?  
    import os
# import xml related libraries
    import xml.etree.ElementTree as elementtree

    for root, dirs, files in os.walk(config.gamedir + '/mods'):
        path = root.split('/')
        for file in files:
            if file == ('manifest.xml'):         
                nb_de_mods =  nb_de_mods + 1
                tree = elementtree.parse(root + '/manifest.xml')
                namemod = tree.findtext('name', default='Non disponible')
                if namemod != 'Non disponible': # Si pas de nom, on abandonne
                    if namemod not in persistent.mods: #si nouveau mod on l'ajoute à la liste
                        persistent.mods[namemod] = '0'        
                    version_game_mod = tree.findtext('version_game', default='Non disponible')
                    version_mod = tree.findtext('version_mod', default='Non disponible')
                    place_mod = tree.findtext('place', default=0)
                    character_mod = tree.findtext('character', default=0)
                    discussion_mod = tree.findtext('discussion', default=0)
                    dictionnaire_mods[nb_de_mods] = [namemod, version_mod, version_game_mod, place_mod, character_mod, discussion_mod, persistent.mods[namemod]]
