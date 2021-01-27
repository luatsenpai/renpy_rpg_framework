define m = Character("Mika")

label start:
    show screen map_screen(main_house)
    $occupant = main_house.map[10][8].occupant is None
    "."
    $main_house.moveDenizen(mika.x, mika.y, 0, -1)
    "."
    return