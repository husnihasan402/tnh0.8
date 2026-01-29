define Rogue_all_Clothes["greenblack_boyshorts"] = {
    "name": "черно-зеленые шортики",
    "short_name": "шортики",
    "short_name_rod": "шортиков",
    "short_name_dat": "шортикам",
    "short_name_vin": "шортики",
    "short_name_tvo": "шортиками",
    "short_name_pre": "шортиках",

    "type": "underwear",
    "chapter": 1,
    "season": 2,

    "price": 3,

    "shame": (25, 175),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "ass": (0,),
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

label Rogue_greenblack_boyshorts_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Мне они нравятся!"

    return

label Rogue_greenblack_boyshorts_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Я могу сама купить себе одежду, спасибо."

    return

label Rogue_greenblack_boyshorts_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Ох, спасибо!"

    return

label Rogue_greenblack_boyshorts_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Нет, спасибо, [Player.first_name]."

    return

label Rogue_greenblack_boyshorts_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "[Jean.public_name] не шутила, когда говорила мне, насколько они удобны."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "По правде говоря, я начала надевать их на задания. Очень удобно, когда ничего не выперает под облегающим костюмом."

    return

label Rogue_greenblack_boyshorts_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", eyes = "down")

        ch_Rogue "Так удобно!"

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ну, они, конечно, не особо сексуальные. . ."

    return

label Rogue_greenblack_boyshorts_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "[Jean.public_name] не шутила, когда говорила мне, насколько они удобны."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "По правде говоря, я начала надевать их на задания. Очень удобно, когда ничего не выперает под облегающим костюмом."

    return

label Rogue_greenblack_boyshorts_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", eyes = "down")

        ch_Rogue "Обожаю ходить в них."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Они не самые сексуальные, но мои булочки в них выглядят вполне прилично."

    return
