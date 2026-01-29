define Rogue_all_Clothes["black_leather_skirt"] = {
    "name": "черная кожаная юбка",
    "short_name": "юбка",
    "short_name_rod": "юбки",
    "short_name_dat": "юбке",
    "short_name_vin": "юбку",
    "short_name_tvo": "юбкой",
    "short_name_pre": "юбке",

    "type": "skirt",
    "chapter": 1,
    "season": 4,#6,

    "shame": (20, 35),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        0: {
            "black_jeans": (0, 1, 2),
            "dark_denim_shorts": (0, 1, 2),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        1: {
            "black_jeans": (0, 1, 2),
            "dark_denim_shorts": (0, 1, 2),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)}},
    "obscured_by": {
        0: {
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}},
    "covered_by": {
        0: {
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_black_leather_skirt_shopping_accept:

    return

label Rogue_black_leather_skirt_shopping_reject:

    return

label Rogue_black_leather_skirt_gift_accept:

    return

label Rogue_black_leather_skirt_gift_reject:

    return

label Rogue_black_leather_skirt_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "В ней моя попка выглядит потрясающе, не так ли?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Позже я бы с удовольствием прогулялась с тобой по городу в этой юбке."

    return

label Rogue_black_leather_skirt_change_private_after:
    if approval_check(Rogue, threshold = "see_underwear"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Нравится?"
        elif dice_roll == 2:
            $ Rogue.change_face("sexy")

            ch_Rogue "Когда я сажусь в этой юбке, открывается кое-что интересное. . ."
            ch_Rogue "Хочешь взглянуть?"

    return

label Rogue_black_leather_skirt_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Это не самая скромная юбка, но и не слишком откровенная. . ."

    return

label Rogue_black_leather_skirt_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Сегодня идеальный день, чтобы сверкнуть в городе, тебе так не кажется?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Тебя она не слишком отвлекает?"

    return
