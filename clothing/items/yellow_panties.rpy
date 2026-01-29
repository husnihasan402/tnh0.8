define Rogue_all_Clothes["yellow_panties"] = {
    "name": "желтые трусики",
    "short_name": "трусики",
    "short_name_rod": "трусиков",
    "short_name_dat": "трусикам",
    "short_name_vin": "трусики",
    "short_name_tvo": "трусиками",
    "short_name_pre": "трусиках",

    "type": "underwear",

    "shame": (0, 100),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "pussy": (0,),
            "anus": (0,)},
        "doggy": {
            "pussy": (0,),
            "anus": (0,)},
        "hands_and_knees": {
            "pussy": (0,),
            "anus": (0,)},
        "leaning_back": {
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "pussy": (0,),
            "anus": (0,)},
        "doggy": {
            "pussy": (0,),
            "anus": (0,)},
        "hands_and_knees": {
            "pussy": (0,),
            "anus": (0,)},
        "leaning_back": {
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_jeans": (0, 1, 2),
            "black_tights": (0, 1),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1),
            "green_running_tights": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)}},
    "obscured_by": {
        0: {
            "black_jeans": (0,),
            "black_leather_skirt": (0,),
            "dark_denim_shorts": (0,),
            "green_athletic_shorts": (0,),
            "green_maxi_dress": (0, 1),
            "green_running_tights": (0,),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}},
    "covered_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "black_tights": (0,),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_running_tights": (0,),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_yellow_panties_shopping_accept:

    return

label Rogue_yellow_panties_shopping_reject:

    return

label Rogue_yellow_panties_gift_accept:

    return

label Rogue_yellow_panties_gift_reject:

    return

label Rogue_yellow_panties_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        if approval_check(Rogue, threshold = "see_pussy"):
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("sly")

            ch_Rogue "Хочешь небольшое представление? Думаю, это можно устроить."
        elif dice_roll == 2:
            $  Rogue.change_face("worried1", mouth = "lipbite")

            ch_Rogue "[Rogue.Player_petname!c], возможно, тебе как-нибудь стоит сорвать их с меня."

    return

label Rogue_yellow_panties_change_private_after:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], знаешь, я отлично выгляжу в желтом. . ."
        ch_Rogue "Мне нравится, как он подчеркивает мой образ."
    elif dice_roll == 2:
        $ Rogue.change_face("devious")

        ch_Rogue "Может, мне стоит каждое утро спрашивать тебя, какие трусики надеть? Это сэкономило бы мне кучу времени."

    return

label Rogue_yellow_panties_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Конечно, можно надеть и желтые."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Рада служить, [Rogue.Player_petname]. . ."

        $ Rogue.change_face("sexy")

        ch_Rogue "Все равно мои нынешние намокли."

    return

label Rogue_yellow_panties_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Я надела их, как ты и хотел."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Простые, но удобные."

    return
