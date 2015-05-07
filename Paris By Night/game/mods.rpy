init -1 python:
    nb_de_mods = 0
    if not persistent.mods:
        persistent.mods = {}
    dictionnaire_mods = {}

    
    
    import os
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
                    author_mod = tree.findtext('author', default='Non disponible')
                    version_mod = tree.findtext('version_mod', default='Non disponible')
                    place_mod = tree.findtext('places', default=0)
                    character_mod = tree.findtext('character', default=0)
                    discussion_mod = tree.findtext('discussion', default=0)
                    enquete_mod = tree.findtext('enquete', default=0)
                    enquete_alea_mod = tree.findtext('enquete_alea', default=0)
                    objets_mod = tree.findtext('objets', default=0)
                    chemin_mod = str(os.path.split(root)[1:])[3:-3]
                    dictionnaire_mods[nb_de_mods] = (chemin_mod, namemod, version_mod, author_mod, place_mod, character_mod, discussion_mod, enquete_mod, enquete_alea_mod, objets_mod, persistent.mods[namemod])