define Rogue_all_Clothes["black_cage_bra"] = {
    "name": "черный лифчик в клетку",
    "short_name_rod": "лифчика",
    "short_name_dat": "лифчику",
    "short_name_vin": "лифчик",
    "short_name_tvo": "лифчиком",
    "short_name_pre": "лифчике",
    "short_name": "лифчик",

    "type": "bra",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 6,

    "shame": (10, 200),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "breasts": (0,)}},
    "hides": {
        "standing": {
            "breasts": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_fishnet_top": (0, 1),
            "black_lowcut_top": (0, 1),
            "black_NIN_shirt": (0, 1),
            "brown_classic_jacket": (0, 1),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0, 1),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},
    "obscured_by": {
        0: {
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},
    "covered_by": {
        0: {
            "black_fishnet_top": (0,),
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "brown_classic_jacket": (0,),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},

    "traits": {
        "supports_breasts": [0]}}

label Rogue_black_cage_bra_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Думаешь, мне он подойдет?"

    return

label Rogue_black_cage_bra_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Меня не интересуют твои предпочтения в отношении лифчиков."

    return

label Rogue_black_cage_bra_gift_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "Я могу надеть его для тебя. . ."

    return

label Rogue_black_cage_bra_gift_reject:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Я бы предпочла, чтобы ты не покупал мне лифчики. . ."

    return

label Rogue_black_cage_bra_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("worried1", eyes = "down")

            ch_Rogue "Он довольно сексуальный. . . надену его только потому, что просишь ты. . ."

            $ Rogue.eyes = "neutral"
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Хочешь лучше видеть моих девочек?"

    return

label Rogue_black_cage_bra_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "lipbite")

        ch_Rogue "Разве он не изящный?"

        $ Rogue.change_face("sexy")

        ch_Rogue "Думаю, если бы я была вампиршей-королевой мертвых, он был бы постоянной частью моего гардероба."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Господи, сколько же нижнего белья я хочу показать тебе. . ."

    return

label Rogue_black_cage_bra_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне нравится этот лифчик. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я когда-нибудь говорила тебе, что могу снять лифчик одной рукой?"

    return

label Rogue_black_cage_bra_change_public_after:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("wink")

            ch_Rogue "Я просто обожаю преображаться в вампиршу ради тебя!"
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Надеюсь, никто не увидит. . ."
            ch_Rogue "Кроме тебя, конечно."

    return
