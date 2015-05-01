init -1 python:
    nb_de_mods = 0
    mods_dispo = []
    dictionnaire_mods = {}
    test456 = ['nb_de_mods', 'tong']

# Des mods  sont-ils disponibles ?  
    import os
# import xml related libraries
    import xml.etree.ElementTree as elementtree

    for root, dirs, files in os.walk(config.gamedir + '/mods'):
        path = root.split('/')
        for file in files:
            if file == ('manifest.xml'):         
                nb_de_mods += 1
                tree = elementtree.parse(root + '/manifest.xml')
                namemod = tree.findtext('name', default='Non disponible')
                if not persistent.mods_dispo:
                    if namemod != 'Non disponible':
                        version_game_mod = tree.findtext('version_game', default='Non disponible')
                        version_mod = tree.findtext('version_mod', default='Non disponible')
                        place_mod = tree.findtext('place', default=0)
                        character_mod = tree.findtext('character', default=0)
                        discussion_mod = tree.findtext('discussion', default=0)
                        mods_dispo.append([tree, _(namemod), version_mod, version_game_mod, place_mod, character_mod, discussion_mod, 0])
                else :
                    if persistent.mods_dispo.list(tree) :
                        version_game_mod = tree.findtext('version_game', default='Non disponible')
                        version_mod = tree.findtext('version_mod', default='Non disponible')
                        place_mod = tree.findtext('place', default=0)
                        character_mod = tree.findtext('character', default=0)
                        discussion_mod = tree.findtext('discussion', default=0)
                        mods_dispo.append([tree, _(namemod), version_mod, version_game_mod, place_mod, character_mod, discussion_mod, persistent.mods_dispo[persistent.mods_dispo.index(tree) +1 ] ])
                    else:
                        version_game_mod = tree.findtext('version_game', default='Non disponible')
                        version_mod = tree.findtext('version_mod', default='Non disponible')
                        place_mod = tree.findtext('place', default=0)
                        character_mod = tree.findtext('character', default=0)
                        discussion_mod = tree.findtext('discussion', default=0)
                        mods_dispo.append([tree, _(namemod), version_mod, version_game_mod, place_mod, character_mod, discussion_mod, 0])
  
# à condenser le truc ci-dessus

