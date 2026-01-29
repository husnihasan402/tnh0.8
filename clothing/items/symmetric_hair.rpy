define Rogue_all_Clothes["symmetric"] = {
    "name": "симметричная прическа",
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

label Rogue_symmetric_hair_shopping_accept:

    return

label Rogue_symmetric_hair_shopping_reject:

    return

label Rogue_symmetric_hair_gift_accept:

    return

label Rogue_symmetric_hair_gift_reject:

    return

label Rogue_symmetric_hair_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, дай мне только взять расческу."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Скоро вернусь, [Rogue.Player_petname]. Мне нужно найти расческу."

    return

label Rogue_symmetric_hair_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Такое чувство, что эта прическа никогда не выйдет из моды?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Никак не могу привыкнуть к волосам на своем лице."

    return

label Rogue_symmetric_hair_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, дай мне только взять расческу."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Скоро вернусь, [Rogue.Player_petname]. Мне нужно найти расческу."

    return

label Rogue_symmetric_hair_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Такое чувство, что эта прическа никогда не выйдет из моды?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Никак не могу привыкнуть к волосам на своем лице."

    return
