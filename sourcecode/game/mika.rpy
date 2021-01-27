default k_dir = "down"
default m_status = "stand"

image m_walk = ConditionSwitch(
    "m_status == 'walk'", renpy.easy_displayable("mika walk"),
    "m_status == 'stand'", renpy.easy_displayable("mika stand"),
    predict_all = True)

image mika = "mika [k_dir]"

define k_offset = -56

init python:
    def getFacingTile():
        if k_dir == "up":
            return (mika.x, mika.y + 1)
        elif k_dir == "down":
            return (mika.x, mika.y - 1)
        elif k_dir == "left":
            return (mika.x - 1, mika.y)
        else:
            return (mika.x + 1, mika.y)

    def mikaInteracts():
        x, y = getFacingTile()
        mika_sprite.map.triggerInteraction(x,y)

image mika stand:
    "m[k_dir]2.png"
image mika walk:
    "m[k_dir]1.png"
    0.15
    "m[k_dir]2.png"
    0.2
    "m[k_dir]3.png"
    0.15
    "m[k_dir]2.png"
    0.2

    repeat

image mika down:
    "mdown1.png"
    0.15
    "mdown2.png"
    0.2
    "mdown3.png"
    0.15
    "mdown2.png"
    0.2
    repeat
image mika left:
    "mleft1.png"
    0.15
    "mleft2.png"
    0.2
    "mleft3.png"
    0.15
    "mleft2.png"
    0.2
    repeat
image mika right:
    "mright1.png"
    0.15
    "mright2.png"
    0.2
    "mright3.png"
    0.15
    "mright2.png"
    0.2
    repeat
image mika up:
    "mup1.png"
    0.15
    "mup2.png"
    0.2
    "mup3.png"
    0.15
    "mup2.png"
    0.2
    repeat