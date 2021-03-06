init -1 python:
    nb_de_mods = 0
    if not persistent.mods:
        persistent.mods = {}
    dictionnaire_mods = {}
    liste_dico_mod = ('chemin_mod', 
        'namemod', 
        'version_mod', 
        'author_mod','place_mod', 
        'character_mod', 
        'discussion_mod', 
        'enquete_mod', 
        'enquete_alea_mod', 
        'objets_mod', 
        'mod_actif')
    if not persistent.performance:
        persistent.performance = 25

    config.image_cache_size = persistent.performance
    var_perf = config.image_cache_size
    
    
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
                    liste_var_mods = range(len(liste_dico_mod))
                    mod_actif = persistent.mods[namemod]
                    i = 0
                    for i in range(0,len(liste_dico_mod)) :
                        liste_var_mods[i] = eval(liste_dico_mod[i])
                        i = i+1
                    dictionnaire_mods[nb_de_mods] = liste_var_mods

    def define_images(imageFolder, flip=True):
        path_list_folder = imageFolder.split("/")
        path_list_folder = len(path_list_folder)
        for path_portraits in renpy.list_files():
            if path_portraits.startswith(imageFolder):
                path_list = path_portraits.split("/")   # on split
                path_list[-1] = os.path.splitext(path_list[-1])[0] # on vire l'extension
                path_list = tuple(path_list[path_list_folder:])   # on garde juste l'arborescence post imageFolder
                renpy.image(path_list, path_portraits) # construction de l'image avec le lien
                if flip:
                    renpy.image(path_list + ("flip", ), im.Flip(path_portraits, horizontal=True))