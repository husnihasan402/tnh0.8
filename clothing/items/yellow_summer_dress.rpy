define Rogue_all_Clothes["yellow_summer_dress"] = {
    "name": "желтое летнее платье",
    "short_name_rod": "платья",
    "short_name_dat": "платью",
    "short_name_vin": "платье",
    "short_name_tvo": "платьем",
    "short_name_pre": "платье",
    "short_name": "платье",

    "type": "dress",

    "available_states": {
        "standing": (0, 1, 2, 3)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0, 2),
            "breasts": (0, 2),
            "back": (0, 1, 2, 3),
            "belly": (0, 1, 2, 3),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},
    "hides": {
        "standing": {
            "breasts": (0, 2),
            "back": (0, 1, 2, 3),
            "belly": (0, 1, 2, 3),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (1,),
            "black_keyhole_bra": (1,),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "green_bikini_top": (1,),
            "green_lace_bra": (1,),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        1: {
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        2: {
            "black_cage_bra": (1,),
            "black_keyhole_bra": (1,),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "green_bikini_top": (1,),
            "green_lace_bra": (1,),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        3: {
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},

        "take_off": {
            "black_NIN_shirt": (0, 1),
            "brown_classic_jacket": (0, 1),
            "greybrown_plaid_jacket": (1,)}},
    "obscured_by": {
        0: {
            "towel": (0,)},
        1: {
            "towel": (0,)},
        2: {
            "towel": (0,)},
        3: {
            "towel": (0,)}},
    "covered_by": {
        0: {
            "greybrown_plaid_jacket": (1,),
            "towel": (0, 1)},
        1: {
            "greybrown_plaid_jacket": (1,),
            "towel": (0, 1)},
        2: {
            "greybrown_plaid_jacket": (1,),
            "towel": (0, 1)},
        3: {
            "greybrown_plaid_jacket": (1,),
            "towel": (0, 1)}}}

label Rogue_yellow_summer_dress_shopping_accept:
    $ Rogue.change_face("happy")
    $ Rogue.change_arms("sass")

    ch_Rogue "Оно {i}очень{/i} милое."

    if Rogue in Partners:
        $ Rogue.change_arms("hips", left_arm = "rub_neck")

        ch_Rogue "Я буду часто его надевать для тебя."

    return

label Rogue_yellow_summer_dress_shopping_reject:
    $ Rogue.change_face("confused1")
    $ Rogue.change_arms("crossed")

    ch_Rogue "Не очень хочу, чтобы ты покупал мне платья. . ."

    return

label Rogue_yellow_summer_dress_gift_accept:
    $ Rogue.change_face("sly")
    $ Rogue.change_arms("hips", left_arm = "extended")

    ch_Rogue "Я видела такое в магазине."

    if Rogue in Partners:
        $ Rogue.change_arms("sheepish", right_arm = "extended")

        ch_Rogue "Рада, что ты хочешь видеть меня в нем так же сильно, как я хочу надеть его для тебя. . ."

    return

label Rogue_yellow_summer_dress_gift_reject:
    $ Rogue.change_face("confused2")
    $ Rogue.change_arms("crossed")

    ch_Rogue "Оно милое, но. . . я не знаю, почему ты решил, что я буду не против, если ты купишь его для меня."

    return

label Rogue_yellow_summer_dress_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, оно очень милое, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я давно хотела снова его надеть."

    return

label Rogue_yellow_summer_dress_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sly", blush = 1)

            ch_Rogue "Я не виновата, что захватила все твое внимание. . ."
            ch_Rogue "Ты сам меня попросил."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy")

            ch_Rogue "Можешь хорошо меня рассмотреть. Я знаю, тебе нравится, как выглядит моя попка в этом платье. . ."

    return

label Rogue_yellow_summer_dress_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, мне очень нравится это платье. Я не против носить его всегда."
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Я буду надевать это платье, когда ты захочешь."
        ch_Rogue "Оно очень удобное {i}и{/i} очень милое."

    return

label Rogue_yellow_summer_dress_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Крутое, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk")

        ch_Rogue "Соберись, пока люди не заметили, как ты пялишься на меня. . ."

    return
