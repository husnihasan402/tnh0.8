define Rogue_all_Clothes["green_lace_panties"] = {
    "name": "зеленые кружевные трусики",
    "short_name": "трусики",
    "short_name_rod": "трусиков",
    "short_name_dat": "трусикам",
    "short_name_vin": "трусики",
    "short_name_tvo": "трусиками",
    "short_name_pre": "трусиках",

    "type": "underwear",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 4,

    "shame": (20, 310),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_jeans": (0, 1, 2),
            "black_tights": (0, 1),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1),
            "green_running_tights": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)}},
    "obscured_by": {
        0: {
            "black_jeans": (0,),
            "black_leather_skirt": (0,),
            "dark_denim_shorts": (0,),
            "green_athletic_shorts": (0,),
            "green_maxi_dress": (0, 1),
            "green_running_tights": (0,),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}},
    "covered_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "black_tights": (0,),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_running_tights": (0,),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_green_lace_panties_shopping_accept:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("smirk2")

    ch_Rogue "У меня никогда раньше не было кружевных трусиков."

    return

label Rogue_green_lace_panties_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Я сама могу выбрать себе нижнее белье, спасибо."

    return

label Rogue_green_lace_panties_gift_accept:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Хм, они мне подойдут."

    return

label Rogue_green_lace_panties_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Не думаю, что это уместно. . ."

    return

label Rogue_green_lace_panties_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Лучшее, что есть в моей нынешней жизни. . . все варианты нижнего белья."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Желаешь лучше все рассмотреть?"

    return

label Rogue_green_lace_panties_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "Мне всегда приятно надевать что-то подобное для тебя."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Кружева смотрятся на мне потрясающе, правда?"

    return

label Rogue_green_lace_panties_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Те, что на мне, слегка намокли. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Меня заводит наряжаться для тебя. Лучше бы тебе сегодня вечером сорвать с меня свои подарки. . ."

    return

label Rogue_green_lace_panties_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне они очень идут."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Не перевозбудись, [Rogue.Player_petname]."
        ch_Rogue "Хотя кого я обманываю, я уже сама на грани."

    return
