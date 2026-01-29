define Rogue_all_Clothes["towel"] = {
    "name": "полотенце",
    "short_name": "полотенце",
    "short_name_rod": "полотенца",
    "short_name_dat": "полотенцу",
    "short_name_vin": "полотенце",
    "short_name_tvo": "полотенцем",
    "short_name_pre": "полотенце",

    "type": "towel",

    "shame": (0, 500),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,),
            "belly": (0,),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,),
            "belly": (0,),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        0: {
            "green_lace_nighty": (1,),
            "green_maxi_dress": (0, 1),
            "green_mesh_top": (0, 1),
            "greenyellow_classic_suit": (1,)},
        1: {
            "green_maxi_dress": (0, 1),
            "green_mesh_top": (0, 1),
            "greenyellow_classic_suit": (1,)}}}

label Rogue_towel_shopping_accept:

    return

label Rogue_towel_shopping_reject:

    return

label Rogue_towel_gift_accept:

    return

label Rogue_towel_gift_reject:

    return

label Rogue_towel_change_private_before:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1")

            ch_Rogue "Ну, если ты хочешь."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy")

            ch_Rogue "Хочешь увидеть меня в одном лишь полотенце? Пожалуй, это можно устроить."

    return

label Rogue_towel_change_private_after:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Rogue "[Rogue.Player_petname!c], в таком виде я наверняка привлеку всеобщее внимание."
    elif dice_roll == 2:
        $ Rogue.change_face("sly", blush = 2)

        ch_Rogue "[Rogue.Player_petname!c], мне немного холодно, но. . ."
        ch_Rogue "Я сейчас чувствую себя очень сексуальной."

    return

label Rogue_towel_change_public_before:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1")

            ch_Rogue "Ну, если ты хочешь."
        elif dice_roll == 2:
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

            ch_Rogue "Хочешь увидеть меня в одном лишь полотенце? Пожалуй, это можно устроить."

    return

label Rogue_towel_change_public_after:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Rogue "[Rogue.Player_petname!c], в таком виде я наверняка привлеку всеобщее внимание."
    elif dice_roll == 2:
        $ Rogue.change_face("sly", blush = 2)

        ch_Rogue "[Rogue.Player_petname!c], мне немного холодно, но. . ."
        ch_Rogue "Я сейчас чувствую себя очень сексуальной."

    return
