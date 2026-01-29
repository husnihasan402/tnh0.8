define Rogue_all_Clothes["green_thong"] = {
    "name": "зеленые стринги",
    "short_name": "стринги",
    "short_name_rod": "стринг",
    "short_name_dat": "стрингам",
    "short_name_vin": "стринги",
    "short_name_tvo": "стрингами",
    "short_name_pre": "стрингах",

    "type": "underwear",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 3,

    "shame": (40, 375),

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

label Rogue_green_thong_shopping_accept:
    $ Rogue.change_face("happy")

    ch_Rogue "Это мне? И к тому же в моем любимом цвете?"

    if approval_check(Rogue, threshold = "sexual_flirting"):
        ch_Rogue "Они очень сексуальные, я хочу надеть их прямо сейчас для тебя."

    return

label Rogue_green_thong_shopping_reject:
    $ Rogue.change_face("confused3")

    ch_Rogue "Я ценю твой жест, но, [Rogue.Player_petname], мы еще не достигли такого этапа отношений, когда ты можешь покупать мне трусики."

    return

label Rogue_green_thong_gift_accept:
    $ Rogue.change_face("happy")

    ch_Rogue "Это мне? И к тому же в моем любимом цвете?"

    if approval_check(Rogue, threshold = "sexual_flirting"):
        ch_Rogue "Они очень сексуальные, я хочу надеть их прямо сейчас для тебя."

    return

label Rogue_green_thong_gift_reject:
    $ Rogue.change_face("confused3")

    ch_Rogue "Я ценю твой жест, но, [Rogue.Player_petname], мы еще не достигли такого этапа отношений, когда ты можешь покупать мне трусики."

    return

label Rogue_green_thong_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", mouth = "lipbite")

        ch_Rogue "Хочешь, чтобы я надела их для тебя, да?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Желаешь получше все разглядеть?"

    return

label Rogue_green_thong_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Что скажешь? В них я ведь выгляжу сексуально, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Ну как? Нравится?"

    return

label Rogue_green_thong_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sly")

            ch_Rogue "Не мог дождаться, когда мы вернемся в одну из наших комнат?"
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Желаешь получше все разглядеть?"

    return

label Rogue_green_thong_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Что скажешь? В них я ведь выгляжу сексуально, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Ну как? Нравится?"

    return
