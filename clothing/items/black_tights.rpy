define Rogue_all_Clothes["black_tights"] = {
    "name": "черные колготки",
    "short_name": "колготки",
    "short_name_rod": "колготок",
    "short_name_dat": "колготкам",
    "short_name_vin": "колготки",
    "short_name_tvo": "колготками",
    "short_name_pre": "колготках",

    "type": "hose",

    "shame": (-5, -5),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "thighs": (0,),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,),
            "feet": (0, 1)}},

    "blocked_by": {
        0: {
            "black_ankle_socks": (0,),
            "black_cage_thong": (1,),
            "black_stockings": (0,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        1: {
            "black_ankle_socks": (0,),
            "black_stockings": (0,)},

        "take_off": {
            "black_heels": (0,),
            "black_jeans": (0, 1, 2),
            "black_strap_pumps": (0,),
            "black_thighhigh_boots": (0,),
            "blackgreen_sneakers": (0,),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "yellow_classic_boots": (0,)}},
    "obscured_by": {
        0: {
            "black_jeans": (0,),
            "greenyellow_classic_suit": (0, 1),
            "towel": (0,)}},
    "covered_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_lace_nighty": (0, 1),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_black_tights_shopping_accept:

    return

label Rogue_black_tights_shopping_reject:

    return

label Rogue_black_tights_gift_accept:

    return

label Rogue_black_tights_gift_reject:

    return

label Rogue_black_tights_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk1")

        ch_Rogue "Надеюсь, в ближайшее время мне не придется бегать."

        if approval_check(Rogue, threshold = "sexual_flirting"):
            $ Rogue.change_face("sly")

            ch_Rogue "Мне нравится, что тебя привлекают мои ножки, но не забывай и о моих руках."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Тебя они заводят?"

    return

label Rogue_black_tights_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("wink")

            ch_Rogue "К слову, они до самой талии"

            $ Rogue.change_face("sly")

            ch_Rogue "Если хочешь, могу немного приспустить. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy")

            ch_Rogue "Уверена, я выгляжу как твоя личная танцовщица. . ."

    return

label Rogue_black_tights_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "После того, как я их надеу, мне бы хотелось сходить в тот стейк-хаус."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Колготки под юбкой - отличный способ сохранить скромность. . ."

    return

label Rogue_black_tights_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sly")

            ch_Rogue "Тебе стоит увлекаться не только ножками. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy")

            ch_Rogue "К слову, они до самой талии."

    return
