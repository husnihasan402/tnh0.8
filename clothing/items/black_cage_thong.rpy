define Rogue_all_Clothes["black_cage_thong"] = {
    "name": "черные стринги в клетку",
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

    "price": 5,

    "shame": (15, 350),

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
            "black_leather_skirt": (0,),
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

label Rogue_black_cage_thong_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Ух ты, какие сексуальные."

    $ Rogue.change_face("worried1")

    ch_Rogue "Но не {i}слишком{/i} сексуальные, правда?"

    return

label Rogue_black_cage_thong_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Ага. . . но нет. . ."

    return

label Rogue_black_cage_thong_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Блин, [Player.first_name]."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Интересно, почему они тебе так нравятся. . ."

    return

label Rogue_black_cage_thong_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Зачем мне вообще принимать такой подарок. . . ?"

    return

label Rogue_black_cage_thong_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Не думаю, что у меня когда-нибудь будет достаточно нижнего белья."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Они не оставляют простора для воображения. . ."
        ch_Rogue "Но мне нравится выражение твоего лица сейчас."

    return

label Rogue_black_cage_thong_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

        ch_Rogue "Мне кажется, я видела что-то похожее в каком-то старом научно-фантастическом фильме."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "Интересно, почему они тебе так нравятся. . ."

        $ Rogue.eyes = "neutral"

    return

label Rogue_black_cage_thong_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Те, что на мне, слегка намокли. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Желаешь рассмотреть все получше?"

    return

label Rogue_black_cage_thong_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue " [Rogue.Player_petname], что думаешь?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Они очень. . . тонкие."

    return
