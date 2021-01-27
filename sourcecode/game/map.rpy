define tile_size = 80


init python:

    
    class TestMap:
        def __init__(self, map_grid, img, start_x, start_y):
            self.map = map_grid
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty(self, x, y):
            return self.map[y][x].occupant is None

        def occupy(self, x, y, denizen):
            if not self.isEmpty(x, y):
                return
            self.map[y][x].occupant = denizen
            denizen.x = x
            denizen.y = y
            denizen.map = self

        def unoccupy(self, x, y):
            self.map[y][x].occupant = None

        def overlayimg(self, image):
            self.image = image

        def moveDenizen(self, x, y, offx, offy):
            if self.isEmpty(x,y):
                return
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                return
            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y + offy][x + offx].occupant = denizen
            denizen.x += offx
            denizen.y += offy

            if self.center_x == x and self.center_y == y:
                self.center_x += offx
                self.center_y += offy

        def triggerInteraction(self, x, y):
            if x < 0 or x >= len (self.map[0]):
                return
            if y < 0 or y >= len(self.map):
                return
            if self.isEmpty(x,y):
                return
            self.map[y][x].occupant.interact()




    class MapTile:
            def __init__(self, occupant=None):
                self.occupant = occupant


    class MapOccupant:
        def __init__(self, x, y, map=None):
            self.x = x
            self.y = y
            self.map = map

        def interact(self):
            pass

        def unoccupy(self):
            if self.map:
                self.map.unoccupy(self.x, self.y)
                self.map = None



    class MapDenizen(MapOccupant):
        def __init__(self, x, y, img, width, height, interaction):
            super(MapDenizen, self).__init__(x,y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction

        def getOffset(self):
            return(tile_size - self.width, tile_size - self.height)

        def interact(self):
            self.interaction(self)

    house_map = []

    for i in range(12):
        new_row = []
        for j in range(19):
           new_row.append(MapTile())
        house_map.append(new_row)

    main_house = TestMap(house_map, "map_hos.png", 6, 6)
    mika = MapDenizen(11, 11, "m_walk", 96, 144, no_op)
    main_house.occupy(6,6,mika)
    wall = MapOccupant(0, 0)
    main_house.occupy(0, 0,wall)
    for uw in range(13):
        main_house.occupy(uw, 3, wall)  #up wall
    for lw in range(11):
        main_house.occupy(0, lw, wall)  #left wall
    for rw in range(11):
        main_house.occupy(13, rw, wall) #right wall
    for dw in range(13):
        main_house.occupy(dw, 8, wall)   #down wall
#   cake_sprite = MapDenizen(5,5, "walking/cupcake.png", 35, 26, disappear)
#   aMap.occupy(5, 5, cake_sprite)

