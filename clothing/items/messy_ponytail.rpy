define Rogue_all_Clothes["messy_ponytail"] = {
    "name": "растрепанный хвост",
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

label Rogue_messy_ponytail_shopping_accept:

    return

label Rogue_messy_ponytail_shopping_reject:

    return

label Rogue_messy_ponytail_gift_accept:

    return

label Rogue_messy_ponytail_gift_reject:

    return

label Rogue_messy_ponytail_change_private_before:
    if approval_check(Rogue, threshold = "blowjob"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Конечно, дай только найду резинку для волос."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Ладно, но растрепанная прическа не означает, что я сразу же наброшусь на тебя. . ."

    return

label Rogue_messy_ponytail_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Обычно я собираю волосы в хвост, когда иду на пробежку, может быть, мы можем потренироваться вместе?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy", eyes = "squint")

        ch_Rogue "Даже не думай ни о чем пошлом. . ."

    return

label Rogue_messy_ponytail_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Конечно, дай только найду резинку для волос."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy", eyes = "squint")

        ch_Rogue "Даже не думай ни о чем пошлом. . ."

    return

label Rogue_messy_ponytail_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Обычно я собираю волосы в хвост, когда иду на пробежку, может быть, мы можем потренироваться вместе?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Я знаю, что люди будут пялиться, но клянусь, прическа специально выглядит растрепанной."

    return
