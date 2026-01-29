define Rogue_all_Clothes["black_sports_bra"] = {
    "name": "черный спортивный лифчик",
    "short_name_rod": "лифчика",
    "short_name_dat": "лифчику",
    "short_name_vin": "лифчик",
    "short_name_tvo": "лифчиком",
    "short_name_pre": "лифчике",
    "short_name": "лифчик",

    "type": "bra",

    "shame": (-15, 35),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "breasts": (0,)}},
    "hides": {
        "standing": {
            "breasts": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_fishnet_top": (0, 1),
            "black_lowcut_top": (0, 1),
            "black_NIN_shirt": (0, 1),
            "brown_classic_jacket": (0, 1),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0, 1),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},
    "obscured_by": {
        0: {
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},
    "covered_by": {
        0: {
            "black_fishnet_top": (0,),
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "brown_classic_jacket": (0,),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},

    "traits": {
        "supports_breasts": [0]}}

label Rogue_black_sports_bra_shopping_accept:

    return

label Rogue_black_sports_bra_shopping_reject:

    return

label Rogue_black_sports_bra_gift_accept:

    return

label Rogue_black_sports_bra_gift_reject:

    return

label Rogue_black_sports_bra_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Мне он нравится. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мы собираемся устроить спарринг?"

    return

label Rogue_black_sports_bra_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Мне тяжело понять, как эта штука умудряется удерживать мои сиськи."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Возможно, позже мы сможем позаниматься наедине."

    return

label Rogue_black_sports_bra_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Мне он нравится. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Забавно, но, пожалуй, это единственная часть моего костюма, которую я никогда не рвала."

    return

label Rogue_black_sports_bra_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Эта штука иногда становится такой мокрой от пота."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я когда-нибудь говорила тебе, что могу снять лифчик одной рукой?"

    return
