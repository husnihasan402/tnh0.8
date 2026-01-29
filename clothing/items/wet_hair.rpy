define Rogue_all_Clothes["wet"] = {
    "name": "мокрые волосы",
    "short_name": "hair",

    "type": "hair",

    "shop_type": "salon",

    "available_states": {
        "standing": (0,),
        "doggy": (0,),
        "hands_and_knees": (0,),
        "leaning_back": (0,),
        "missionary": (0,)},
    "undressed_states": {
        "standing": 0,
        "doggy": 0,
        "hands_and_knees": 0,
        "leaning_back": 0,
        "missionary": 0}}

label Rogue_wet_hair_shopping_accept:

    return

label Rogue_wet_hair_shopping_reject:

    return

label Rogue_wet_hair_gift_accept:

    return

label Rogue_wet_hair_gift_reject:

    return

label Rogue_wet_hair_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("perplexed")

        ch_Rogue "Конечно. . . пойду смочу волосы под краном. . ."

    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Тебе нравится, когда влажные волосы зачесаны назад, да?"

    return

label Rogue_wet_hair_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], теперь они достаточно влажные для тебя?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ну как?"

    return

label Rogue_wet_hair_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Сейчас вернусь, [Rogue.Player_petname]. Нужно найти раковину или пруд."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Тебе нравится, когда влажные волосы зачесаны назад, да?"

    return

label Rogue_wet_hair_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], теперь они достаточно влажные для тебя?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ну как?"

    return
