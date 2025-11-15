define tile_size = 80

screen map_screen(aMap):

    add "#000"

    # Canh giữa map theo center_x, center_y
    $ offset_x = 640 - (tile_size * aMap.center_x) + 40
    $ offset_y = 280 - (tile_size * aMap.center_y) + 40
    add aMap.img:
        pos(offset_x, offset_y)

    # Vẽ toàn bộ occupant trên map
    for y in range(len(aMap.map)):
        $ row = aMap.map[y]
        for x in range(len(row)):
            $ tile = row[x]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $ offx, offy = tile.occupant.getOffset()
                $ tile_lc_x = tile_size * x + offset_x
                $ tile_lc_y = tile_size * y + offset_y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)

    # Timer: cứ 0.12 giây gọi mika_step một lần
    # Nếu m_status == "walk" -> bước liên tục theo k_dir
    timer 0.12 repeat True action Function(mika_step, aMap)

    # --- Điều khiển di chuyển: chỉ set hướng + trạng thái ---

    # LÊN
    key "K_UP" action [
        SetVariable("k_dir", "up"),
        SetVariable("m_status", "walk")
    ]
    key "keyup_K_UP" action [
        SetVariable("k_dir", "up"),
        SetVariable("m_status", "stand")
    ]

    # XUỐNG
    key "K_DOWN" action [
        SetVariable("k_dir", "down"),
        SetVariable("m_status", "walk")
    ]
    key "keyup_K_DOWN" action [
        SetVariable("k_dir", "down"),
        SetVariable("m_status", "stand")
    ]

    # TRÁI
    key "K_LEFT" action [
        SetVariable("k_dir", "left"),
        SetVariable("m_status", "walk")
    ]
    key "keyup_K_LEFT" action [
        SetVariable("k_dir", "left"),
        SetVariable("m_status", "stand")
    ]

    # PHẢI
    key "K_RIGHT" action [
        SetVariable("k_dir", "right"),
        SetVariable("m_status", "walk")
    ]
    key "keyup_K_RIGHT" action [
        SetVariable("k_dir", "right"),
        SetVariable("m_status", "stand")
    ]

    # Tương tác
    key "K_RETURN" action Function(mikaInteracts)


# Các default cũ (nếu bạn đang dùng) – giữ nguyên cho an toàn
default sprite1 = "mika"
default sprite1_walk = "k_walk"
default sprite1_x = 6
default sprite1_y = 6
