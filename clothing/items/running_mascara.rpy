define Rogue_all_Clothes["running_mascara"] = {
    "name": "потекшая тушь",
    "short_name": "тушь",

    "type": "makeup",

    "shop_type": "event",

    "shame": (0, 50),

    "available_states": {
        "standing": (0,),
        "doggy": (0,),
        "hands_and_knees": (0,),
        "leaning_back": (0,),
        "missionary": (0,),
        "supine_paizuri": (0,)},
    "undressed_states": {
        "standing": 0,
        "doggy": 0,
        "hands_and_knees": 0,
        "leaning_back": 0,
        "missionary": 0,
        "supine_paizuri": 0}}

label Rogue_running_mascara_shopping_accept:

    return

label Rogue_running_mascara_shopping_reject:

    return

label Rogue_running_mascara_gift_accept:

    return

label Rogue_running_mascara_gift_reject:

    return

label Rogue_running_mascara_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь, чтобы я выглядела как настоящая металлюга?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "А ты смелый, раз просишь меня испортить свой макияж."

    return

label Rogue_running_mascara_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Вот что я тебе скажу: думаю, я выгляжу по-странному сексуально."
    elif dice_roll == 2:
        $ Rogue.change_face("sly", blush = 1)

        ch_Rogue "Так устроит?"

    return

label Rogue_running_mascara_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь, чтобы я выглядела как настоящая металлюга?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "А ты смелый, раз просишь меня испортить свой макияж."

    return

label Rogue_running_mascara_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Вот что я тебе скажу: думаю, я выгляжу по-странному сексуально."
    elif dice_roll == 2:
        $ Rogue.change_face("sly", blush = 1)

        ch_Rogue "Так устроит?"

    return
