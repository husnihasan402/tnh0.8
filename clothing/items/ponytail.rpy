define Rogue_all_Clothes["ponytail"] = {
    "name": "хвост",
    "short_name": "ponytail",

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

label Rogue_ponytail_shopping_accept:

    return

label Rogue_ponytail_shopping_reject:

    return

label Rogue_ponytail_gift_accept:

    return

label Rogue_ponytail_gift_reject:

    return

label Rogue_ponytail_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я всегда ношу резинку для волос."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Конечно, дай только найду резинку для волос."

    return

label Rogue_ponytail_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Обычно я собираю волосы в хвост, когда иду на пробежку, может быть, мы можем потренироваться вместе?"
    elif dice_roll == 2:
        $ Rogue.change_face("wink")

        ch_Rogue "Ты этого хотел?"

    return

label Rogue_ponytail_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я всегда ношу резинку для волос."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Конечно, дай только найду резинку для волос."

    return

label Rogue_ponytail_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Обычно я собираю волосы в хвост, когда иду на пробежку, может быть, мы можем потренироваться вместе?"
    elif dice_roll == 2:
        $ Rogue.change_face("wink")

        ch_Rogue "Ты этого хотел?"

    return
