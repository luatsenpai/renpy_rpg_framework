


screen map_screen(aMap):

    add "#000"

    $ offset_x = 640 - (80 * aMap.center_x) + 40
    $ offset_y = 280 - (80 * aMap.center_y) + 40
    add aMap.img:
        pos(offset_x, offset_y)

    for i in range (len(aMap.map)):
        $ row = aMap.map[i]
        for j in range(len(row)):
            $ tile = row[j]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $ offx, offy = tile.occupant.getOffset()
                $ tile_lc_x = 80 * j + offset_x
                $ tile_lc_y = 80 * i + offset_y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)
    key "K_UP" action [Function(aMap.moveDenizen, mika.x, mika.y, 0, -1), SetVariable("k_dir", "up"), SetVariable("m_status", "walk")]
    key "keyup_K_UP" action [Function(aMap.moveDenizen, mika.x, mika.y, 0, -1), SetVariable("k_dir", "up"), SetVariable("m_status", "stand")]
    key "repeat_K_UP" action [Function(aMap.moveDenizen, mika.x, mika.y, 0, -1), SetVariable("k_dir", "up"), SetVariable("m_status", "walk")]
    key "K_DOWN" action [Function(aMap.moveDenizen, mika.x, mika.y, 0, 1), SetVariable("k_dir", "down"), SetVariable("m_status", "walk")]
    key "keyup_K_DOWN" action [Function(aMap.moveDenizen, mika.x, mika.y, 0, 1), SetVariable("k_dir", "down"), SetVariable("m_status", "stand")]
    key "repeat_K_DOWN" action [Function(aMap.moveDenizen, mika.x, mika.y, 0, 1), SetVariable("k_dir", "down"), SetVariable("m_status", "walk")]
    key "K_LEFT" action [Function(aMap.moveDenizen, mika.x, mika.y, -1, 0), SetVariable("k_dir", "left"), SetVariable("m_status", "walk")]
    key "keyup_K_LEFT" action [Function(aMap.moveDenizen, mika.x, mika.y, -1, 0), SetVariable("k_dir", "left"), SetVariable("m_status", "stand")]
    key "repeat_K_LEFT" action [Function(aMap.moveDenizen, mika.x, mika.y, -1, 0), SetVariable("k_dir", "left"), SetVariable("m_status", "walk")]
    key "K_RIGHT" action [Function(aMap.moveDenizen, mika.x, mika.y, 1, 0), SetVariable("k_dir", "right"), SetVariable("m_status", "walk")]
    key "keyup_K_RIGHT" action [Function(aMap.moveDenizen, mika.x, mika.y, 1, 0), SetVariable("k_dir", "right"), SetVariable("m_status", "stand")]
    key "repeat_K_RIGHT" action [Function(aMap.moveDenizen, mika.x, mika.y, 1, 0), SetVariable("k_dir", "right"), SetVariable("m_status", "walk")]
    key "K_RETURN" action Function(mikaInteracts)


default sprite1 = "mika"
default sprite1_walk = "k_walk"
default sprite1_x = 6
default sprite1_y = 6