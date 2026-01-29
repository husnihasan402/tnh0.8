define Rogue_all_Clothes["black_lowcut_top"] = {
    "name": "черный топ с глубоким вырезом",
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
    "hides": {
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
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)},
        1: {
            "green_lace_nighty": (0, 1, 2, 3),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)}}}

label Rogue_black_lowcut_top_shopping_accept:

    return

label Rogue_black_lowcut_top_shopping_reject:

    return

label Rogue_black_lowcut_top_gift_accept:

    return

label Rogue_black_lowcut_top_gift_reject:

    return

label Rogue_black_lowcut_top_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Он очень милый."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "В прошлой жизни я даже представить не могла, что кода-нибудь буду носить что-то подобное."

    return

label Rogue_black_lowcut_top_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sly")

            ch_Rogue "Интересно, почему ты хотел, чтобы я надела его. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy")

            ch_Rogue "[Rogue.Player_petname!c], я не против, когда ты пялишься на меня."
            ch_Rogue "Честно говоря, мне даже нравится."

    return

label Rogue_black_lowcut_top_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Он очень милый."
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Он невероятно спасает в очень жаркие деньки."

    return

label Rogue_black_lowcut_top_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "Честно говоря, я думаю, что некоторые девушки завидуют моей груди."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], я не против, когда ты пялишься на меня."
        ch_Rogue "Честно говоря, мне даже нравится."

    return
