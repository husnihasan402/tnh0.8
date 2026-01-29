define Rogue_all_Clothes["black_keyhole_bra"] = {
    "name": "черный лифчик с вырезом",
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

    "shame": (20, 210),

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
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},

    "traits": {
        "supports_breasts": [0]}}

label Rogue_black_keyhole_bra_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Ого, он такой милый. . ."

    return

label Rogue_black_keyhole_bra_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ты забегаешь вперед, сладенький."

    return

label Rogue_black_keyhole_bra_gift_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "Мне нравится. . ."

    return

label Rogue_black_keyhole_bra_gift_reject:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Эм, нет, спасибо. . ."

    return

label Rogue_black_keyhole_bra_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", eyes = "down")

        ch_Rogue "Он такой милый. . ."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь лучше разглядеть моих девочек?"

    return

label Rogue_black_keyhole_bra_change_private_after:
    if approval_check(Rogue, threshold = "see_breasts"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне кажется, что-то похожее я видела в каком-то старогм научно-фантастическом фильмае."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Ради тебя я могла бы ходить топлесс, но в этом лифчике тоже неплохо. . ."

    return

label Rogue_black_keyhole_bra_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне очень нравится этот лифчик."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ты даже не представляешь, как меня спасает этот лифчик. . ."
        ch_Rogue "Без него моей спине не очень хорошо."

    return

label Rogue_black_keyhole_bra_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я чувствую себя очень сексуальной."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне столько нижнего белья хочется продемонстрировать тебе. . ."

    return
