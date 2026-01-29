define Rogue_all_Clothes["black_fishnet_top"] = {
    "name": "черный топ в сеточку",
    "short_name": "топ",
    "short_name_rod": "топа",
    "short_name_dat": "топу",
    "short_name_vin": "топ",
    "short_name_tvo": "топом",
    "short_name_pre": "топе",

    "type": "top",

    "shame": (15, 15),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,),
            "belly": (0,)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (1,),
            "black_keyhole_bra": (1,),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "green_bikini_top": (1,),
            "green_lace_bra": (1,),
            "green_lace_nighty": (0, 1, 2, 3),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)},
        1: {
            "green_lace_nighty": (0, 1, 2, 3),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)},

        "take_off": {
            "black_NIN_shirt": (0, 1),
            "greybrown_plaid_jacket": (1,)}},
    "covered_by": {
        0: {
            "black_NIN_shirt": (0,),
            "greybrown_plaid_jacket": (1,)},
        1: {
            "black_NIN_shirt": (0,),
            "greybrown_plaid_jacket": (1,)}}}

label Rogue_black_fishnet_top_shopping_accept:

    return

label Rogue_black_fishnet_top_shopping_reject:

    return

label Rogue_black_fishnet_top_gift_accept:

    return

label Rogue_black_fishnet_top_gift_reject:

    return

label Rogue_black_fishnet_top_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Теперь я буду выглядеть как персонаж из одного моего любимого музыкального клипа."
    elif dice_roll == 2:
        $ Rogue.change_face ("pleased2")

        ch_Rogue "Разве это не самая крутая штука на свете?"

    return

label Rogue_black_fishnet_top_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Нравится?"
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Под него лучше что-нибудь надевать."

            if approval_check(Rogue, threshold = "see_breasts"):
                ch_Rogue "Если только ты не хочешь, чтобы я. . ."

    return

label Rogue_black_fishnet_top_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Я считаю, что больше девушек должны надевать сетчатые топы. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне очень нравится, что он соответствует моему стилю."

    return

label Rogue_black_fishnet_top_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face ("pleased2")

        ch_Rogue "Разве сетчатый топ не самая крутая вещь на свете?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Нравится?"

    return
