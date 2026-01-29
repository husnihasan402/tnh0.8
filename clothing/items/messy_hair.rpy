define Rogue_all_Clothes["messy"] = {
    "name": "растрепанные волосы",
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

label Rogue_messy_hair_shopping_accept:

    return

label Rogue_messy_hair_shopping_reject:

    return

label Rogue_messy_hair_gift_accept:

    return

label Rogue_messy_hair_gift_reject:

    return

label Rogue_messy_hair_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("perplexed")

        ch_Rogue "Конечно, сейчас все сделаю. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Не знаю, зачем я вообще приводила себя в порядок сегодня утром."

    return

label Rogue_messy_hair_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("wink")

            ch_Rogue "Я теперь выгляжу так, будто мы только что с сеновала."
        elif dice_roll == 2:
            $ Rogue.change_face("wink")

            ch_Rogue "Тебе нравится, когда я выгляжу так, будто я только что встала с кровати?"
            ch_Rogue ". . . ну или {i}мы{/i}. . . вместе. . ."

    return

label Rogue_messy_hair_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("perplexed")

        ch_Rogue "Конечно, сейчас все сделаю. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Не знаю, зачем я вообще приводила себя в порядок сегодня утром."

    return

label Rogue_messy_hair_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("wink")

            ch_Rogue "Я теперь выгляжу так, будто мы только что с сеновала."
        elif dice_roll == 2:
            $ Rogue.change_face("wink")

            ch_Rogue "Тебе нравится, когда я выгляжу так, будто я только что встала с кровати?"
            ch_Rogue ". . . ну или {i}мы{/i}. . . вместе. . ."

    return
