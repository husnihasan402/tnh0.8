define Rogue_all_Clothes["green_lace_bra"] = {
    "name": "зеленое кружевное бра",
    "short_name_rod": "бра",
    "short_name_dat": "бра",
    "short_name_vin": "бра",
    "short_name_tvo": "бра",
    "short_name_pre": "бра",
    "short_name": "бра",

    "type": "bra",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 5,

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
            "green_maxi_dress": (0,),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},

    "traits": {
        "supports_breasts": [0]}}

label Rogue_green_lace_bra_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Ты думаешь, мне подойдет что-то подобное?"

    return

label Rogue_green_lace_bra_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Мне как-то не по себе от того, что ты выбираешь для меня бра."

    return

label Rogue_green_lace_bra_gift_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "Если тебе повезет, я как-нибудь надену его для тебя."

    return

label Rogue_green_lace_bra_gift_reject:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Я думаю, что еще слишком рано для таких подарков. . ."

    return

label Rogue_green_lace_bra_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Оно немного откровенное. . . но ради тебя я готова. . ."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Желаешь получше рассмотреть моих девочек?"

    return

label Rogue_green_lace_bra_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Не думаю, что у меня когда-либо было что-то настолько изысканное."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Теперь я чувствую себя по-настоящему сексуальной. . ."

    return

label Rogue_green_lace_bra_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Желаешь получше рассмотреть моих девочек?"
        elif dice_roll == 2:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Я когда-нибудь говорила тебе, что могу снять бра одной рукой?"

    return

label Rogue_green_lace_bra_change_public_after:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk1")

        ch_Rogue "Теперь я чувствую себя по-настоящему сексуальной. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Знаешь, [Rogue.Player_petname], я бы сейчас хотела вернуться в одну из наших комнат вместе с тобой."

    return
