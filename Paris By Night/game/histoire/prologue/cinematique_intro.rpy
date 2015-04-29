## Cinématique d'intro du jeu

init:
    image bg = "histoire/prologue/images/images.jpg"

label introduction:

    e "Là on démarre la cinématique d'intro"

    e "Et on affiche le fond"

    scene bg

    e "Puis la worldmap"

    call worldmap_1 from _call_worldmap