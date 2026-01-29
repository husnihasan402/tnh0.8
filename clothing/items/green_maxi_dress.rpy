define Rogue_all_Clothes["green_maxi_dress"] = {
    "name": "зеленое платье",
    "short_name_rod": "платья",
    "short_name_dat": "платью",
    "short_name_vin": "платье",
    "short_name_tvo": "платьем",
    "short_name_pre": "платье",
    "short_name": "платье",

    "type": "dress",

    "chapter": 1,
    "season": 4,

    "price": 10,

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0, 1),
            "belly": (0, 1),
            "thighs": (0, 1),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},
    "hides": {
        "standing": {
            "breasts": (0,),
            "back": (0, 1),
            "belly": (0, 1),
            "thighs": (0, 1),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (0, 1),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "green_bikini_top": (0, 1),
            "green_lace_bra": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        1: {
            "black_cage_bra": (0, 1),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "green_bikini_top": (0, 1),
            "green_lace_bra": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},

        "take_off": {
            "black_NIN_shirt": (0, 1),
            "brown_classic_jacket": (0, 1),
            "greybrown_plaid_jacket": (1,)}},

    "traits": {
        "supports_breasts": [0]}}

label Rogue_green_maxi_dress_shopping_accept:
    $ Rogue.change_face("surprised2")


    ch_Rogue "Господи!"
    ch_Rogue "Мне кажется, оно подойдет даже для красной дорожки. Не могу дождаться, когда надену его!"

    return

label Rogue_green_maxi_dress_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Оно великолепно, но. . ."
    ch_Rogue "Я не могу принять такой подарок."

    return

label Rogue_green_maxi_dress_gift_accept:
    $ Rogue.change_face("surprised2")


    ch_Rogue "Господи!"
    ch_Rogue "Мне кажется, оно подойдет даже для красной дорожки. Не могу дождаться, когда надену его!"

    return

label Rogue_green_maxi_dress_gift_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Оно великолепно, но. . ."
    ch_Rogue "Я не могу принять такой подарок."

    return

label Rogue_green_maxi_dress_change_private_before:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне нравится, какае оно элегантное."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Почему бы нам не сходить куда-нибудь, например, поужинать? Это идеальное платье для вечернего свидания."

    return

label Rogue_green_maxi_dress_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Чтобы научиться ходить в нем, потребовалось. . . какое-то время."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "При желании, я могу задрать подол платья и мы сможем. . ."

    return

label Rogue_green_maxi_dress_change_public_before:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Сделать это здесь будет непросто."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Почему бы нам не сходить куда-нибудь, например, поужинать? Это идеальное платье для вечернего свидания."

    return

label Rogue_green_maxi_dress_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Чтобы научиться ходить в нем, потребовалось. . . какое-то время."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Разве в этом платье моя талия не выглядит невероятно?"

    return
