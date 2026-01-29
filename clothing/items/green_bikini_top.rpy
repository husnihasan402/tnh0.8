define Rogue_all_Clothes["green_bikini_top"] = {
    "name": "зеленый лифчик бикини",
    "short_name": "лифчик бикини",
    "short_name_rod": "лифчика бикини",
    "short_name_dat": "лифчику бикини",
    "short_name_vin": "лифчик бикини",
    "short_name_tvo": "лифчиком бикини",
    "short_name_pre": "лифчике бикини",

    "type": "bra",
    "chapter": 1,
    "season": 2,

    "price": 3,

    "shame": (0, 25),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "breasts": (0,)},
        "doggy": {
            "breasts": (0,)},
        "hands_and_knees": {
            "breasts": (0,)},
        "leaning_back": {
            "breasts": (0,)}},
    "hides": {
        "standing": {
            "breasts": (0,)},
        "doggy": {
            "breasts": (0,)},
        "hands_and_knees": {
            "breasts": (0,)},
        "leaning_back": {
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

label Rogue_green_bikini_top_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Мне нравится зеленый цвет. . ."

    return

label Rogue_green_bikini_top_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Мне как-то не по себе от того, что ты выбираешь для меня бикини. . ."

    return

label Rogue_green_bikini_top_gift_accept:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("smirk2")

    ch_Rogue "Он милый. . ."

    return

label Rogue_green_bikini_top_gift_reject:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("confused1")

    ch_Rogue "Зачем тебе вообще дарить мне бикини?"

    return

label Rogue_green_bikini_top_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь поплавать со мной? Или просто желаешь получше рассмотреть моих девочек?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], я бы не отказалась поплавать."

    return

label Rogue_green_bikini_top_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Немного откровенный. . . но мне нравится зеленый."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "В нем немного прохладно, но мне нравится, как он сидит на мне. . ."

    return

label Rogue_green_bikini_top_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь поплавать со мной? Или просто желаешь получше рассмотреть моих девочек?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], я бы не отказалась поплавать."

    return

label Rogue_green_bikini_top_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Нравится?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        if approval_check(Rogue, threshold = "sexual_flirting"):
            ch_Rogue "По правде говоря, я так много тренировалась, чтобы контролировать свои способности, что могу надеть и снять купальник за несколько секунд."

            $ Rogue.change_face("sly")

        ch_Rogue "Может быть, когда-нибудь мы сможем принять участие в соревнованиях?"

    return
