define Rogue_all_Clothes["brown_classic_jacket"] = {
    "name": "коричневая классическая куртка",
    "short_name_rod": "куртки",
    "short_name_dat": "куртке",
    "short_name_vin": "куртку",
    "short_name_tvo": "курткой",
    "short_name_pre": "куртке",
    "short_name": "куртка",

    "type": "jacket",

    "shame": (-10, -10),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,)}},
    "hides": {
        "standing": {
            "back": (0,)}},

    "blocked_by": {
        0: {
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (1,)},
        1: {
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (1,)}}}

label Rogue_brown_classic_jacket_shopping_accept:

    return

label Rogue_brown_classic_jacket_shopping_reject:

    return

label Rogue_brown_classic_jacket_gift_accept:

    return

label Rogue_brown_classic_jacket_gift_reject:

    return

label Rogue_brown_classic_jacket_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Она не совсем в моем стиле, но без нее я никуда."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Никогда бы не подумала, что ты захочешь, чтобы я надела больше одежды."

    return

label Rogue_brown_classic_jacket_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я ведь хорошо выгляжу в ней, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "В ней я чувствую себя пилотом истребителя."

    return

label Rogue_brown_classic_jacket_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("neutral")

        ch_Rogue "Ага, я не против."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Она не совсем в моем стиле, но без нее я никуда."

    return

label Rogue_brown_classic_jacket_change_public_after:
    if temperature[time_index] < 10:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Она ведь мне идет, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], знаешь, на улице так холодно. . ."

    return
