define Rogue_all_Clothes["black_garterbelt"] = {
    "name": "черный пояс с подвязками",
    "short_name": "пояс с подвязками",
    "short_name_rod": "пояса с подвязками",
    "short_name_dat": "поясу с подвязками",
    "short_name_vin": "пояс с подвязками",
    "short_name_tvo": "поясом с подвязками",
    "short_name_pre": "поясе с подвязками",

    "type": "hose",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 4,

    "shame": (20, 160),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "blocked_by": {
        "take_off": {
            "black_jeans": (0, 1),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0,),
            "greenyellow_classic_suit": (0, 1)}},
    "obscured_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_maxi_dress": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "towel": (0,)}},
    "covered_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_black_garterbelt_shopping_accept:
    $ Rogue.change_face("happy")

    ch_Rogue "Это мне?"

    if Rogue in Partners:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], я с удовольствием надену его для тебя."

    return

label Rogue_black_garterbelt_shopping_reject:
    $ Rogue.change_face("appalled1")

    ch_Rogue "Ты этим хочешь сказать, чтобы я стала твоей госпожой или типа того?"
    ch_Rogue "Извини, [Rogue.Player_petname], я не принимаю такие подарки."

    return

label Rogue_black_garterbelt_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "[Rogue.Player_petname!c], он великолепен. Не думаю, что кто-нибудь когда-либо дарил мне что-то настолько необычное."

    if Rogue in Partners:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], я с удовольствием надену его для тебя."

    return

label Rogue_black_garterbelt_gift_reject:
    $ Rogue.change_face("appalled2")

    ch_Rogue "Я не хочу, чтобы ты покупал мне нижнее белье, особенно такое дорогое."

    return

label Rogue_black_garterbelt_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("perplexed")

        ch_Rogue "Почему подобные вещи такие привлекательные?"

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Это из-за того, что они подчеркивают мой животик?"
        ch_Rogue "Сложно сказать."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Когда я надеваю его, мне становится жарко. . ."
        ch_Rogue "Может быть, позже я позволю тебе снять его с меня."

    return

label Rogue_black_garterbelt_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Ты должен сводить меня в какое-нибудь модное место, я не хочу наряжаться просто так."
            ch_Rogue "Ну, если у тебя, конечно, нет {i}других{/i}планов на сегодняшний вечер. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Обожаю наряжаться для тебя. . ."

    return

label Rogue_black_garterbelt_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Надеюсь, этим я не вскружу слишком много мужских головок."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "В первый раз было нелегко научиться надевать эту штуку."
        ch_Rogue "Но это того стоило, ради выражения твоего лица."

    return

label Rogue_black_garterbelt_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("manic")

            ch_Rogue "Ты должен сводить меня в какое-нибудь модное место, я не хочу наряжаться просто так."
            ch_Rogue "Ну, если у тебя, конечно, нет {i}других{/i}планов на сегодняшний вечер. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Мне теперь хочется сходить в какое-нибудь по-настоящему модное место сегодня вечером."
            ch_Rogue "Думаешь, ты смог бы контролировать себя, зная, что у меня под одеждой?"

    return
