define Rogue_all_Clothes["green_mesh_top"] = {
    "name": "зеленый сетчатый топ",
    "short_name": "топ",
    "short_name_rod": "топа",
    "short_name_dat": "топу",
    "short_name_vin": "топ",
    "short_name_tvo": "топом",
    "short_name_pre": "топе",

    "type": "top",
    "chapter": 1,
    "season": 4,#4

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
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)},
        1: {
            "green_lace_nighty": (0, 1, 2, 3),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)},

        "take_off": {
            "black_NIN_shirt": (0, 1)}},
    "covered_by": {
        0: {
            "black_NIN_shirt": (0,)}}}

label Rogue_green_mesh_top_shopping_accept:

    return

label Rogue_green_mesh_top_shopping_reject:

    return

label Rogue_green_mesh_top_gift_accept:

    return

label Rogue_green_mesh_top_gift_reject:

    return

label Rogue_green_mesh_top_change_private_before:
    if approval_check(Rogue, threshold = "see_breasts"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sly")

            ch_Rogue "Нужно обязательно чтобы под ним что-нибудь было."
            ch_Rogue "Если, конечно, мы собираемся выйти в люди."
        elif dice_roll == 2:
            $ Rogue.change_face ("sexy")

            ch_Rogue "Такое чувство, что ты просто искал предлог, чтобы увидеть меня почти топлесс."

    return

label Rogue_green_mesh_top_change_private_after:
    if "bra" in Rogue.Clothes and approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk1")

        ch_Rogue "Мне очень нравится эта ткань, она подобна облаку."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Тебе нравится?"

    return

label Rogue_green_mesh_top_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Идеальный выбор для хорошей погоды."
    elif dice_roll == 2:
        $ Rogue.change_face ("pleased2")

        ch_Rogue "Разве этот топ не самая красивая вещь на свете?"

    return

label Rogue_green_mesh_top_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Надеюсь, ветер скоро стихнет, мне немного прохладно."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "[Rogue.Player_petname!c], тебе нравится стиль ретро?"

    return
