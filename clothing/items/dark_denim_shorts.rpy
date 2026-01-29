define Rogue_all_Clothes["dark_denim_shorts"] = {
    "name": "темные джинсовые шорты",
    "short_name": "шорты",
    "short_name_rod": "шорт",
    "short_name_dat": "шортам",
    "short_name_vin": "шорты",
    "short_name_tvo": "шортами",
    "short_name_pre": "шортах",

    "type": "pants",

    "shame": (10, 25),

    "available_states": {
        "standing": (0, 1, 2)},
    "undressed_states": {
        "standing": 2},

    "covers": {
        "standing": {
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},
    "hides": {
        "standing": {
            "underwear": (0,),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},

    "blocked_by": {
        0: {
            "black_cage_thong": (1,),
            "black_tights": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        1: {
            "black_cage_thong": (1,),
            "black_tights": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)}},
    "obscured_by": {
        0: {
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)},
        1: {
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
            "yellow_summer_dress": (0, 1)},
        1: {
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_dark_denim_shorts_shopping_accept:

    return

label Rogue_dark_denim_shorts_shopping_reject:

    return

label Rogue_dark_denim_shorts_gift_accept:

    return

label Rogue_dark_denim_shorts_gift_reject:

    return

label Rogue_dark_denim_shorts_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Ах, я так хочу понежиться в них на солнышке."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], хочешь поглазеть на мои ножки?"
        ch_Rogue "Хех, я не против."

    return

label Rogue_dark_denim_shorts_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Хотелось бы, чтобы эти шорты были чуть-чуть длинее. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Ну как, нравится?"

    return

label Rogue_dark_denim_shorts_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Ах, я так хочу понежиться на солнышке в них."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я просто обожаю джинсовые шорты, а все, кто думают иначе, абсолютно неправы."

    return

label Rogue_dark_denim_shorts_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Наконец-то я могу проветриться."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Ну как, нравится?"

    return
