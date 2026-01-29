define Rogue_all_Clothes["black_nipple_tape"] = {
    "name": "черный скотч для сосков",
    "short_name_rod": "скотча для сосков",
    "short_name_dat": "скотчу для сосков",
    "short_name_vin": "скотч для сосков",
    "short_name_tvo": "скотчем для сосков",
    "short_name_pre": "скотче для сосков",
    "short_name": "скотч для сосков",

    "type": "nipple_accessories",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 4,

    "price": 0.5,

    "shame": (0, 500),

    "covers": {
        "standing": {
            "breasts": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_cage_bra": (0,),
            "black_fishnet_top": (0,),
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "black_sports_bra": (0,),
            "black_tanktop": (0,),
            "green_bikini_top": (0,),
            "green_lace_bra": (0,),
            "green_lace_nighty": (0, 2),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "greenyellow_sleeved_swimsuit": (0, 2),
            "towel": (0,),
            "yellow_summer_dress": (0, 2)}},
    "obscured_by": {
        0: {
            "black_cage_bra": (0,),
            "black_fishnet_top": (0,),
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "black_sports_bra": (0,),
            "black_tanktop": (0,),
            "brown_classic_jacket": (0,),
            "green_bikini_top": (0,),
            "green_lace_bra": (0,),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "greenyellow_sleeved_swimsuit": (0, 2),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 2)}},
    "covered_by": {
        0: {
            "black_cage_bra": (0,),
            "black_fishnet_top": (0,),
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "black_sports_bra": (0,),
            "black_tanktop": (0,),
            "brown_classic_jacket": (0,),
            "green_bikini_top": (0,),
            "green_lace_bra": (0,),
            "green_lace_nighty": (0, 2),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "greenyellow_sleeved_swimsuit": (0, 2),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 2)}}}

label Rogue_black_nipple_tape_shopping_accept:
    $ Rogue.change_face("confused1")

    ch_Rogue "Скотч? Я не понимаю. . ."

    $ Rogue.change_face("surprised1")

    ch_Rogue "Ох!"

    $ Rogue.change_face("smirk2")

    return

label Rogue_black_nipple_tape_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Я ничего не понимаю. Спасибо, [Rogue.Player_petname], но, пожалуй, я откажусь."

    return

label Rogue_black_nipple_tape_gift_accept:
    $ Rogue.change_face("sly")

    ch_Rogue "Намек поняла. . ."

    return

label Rogue_black_nipple_tape_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "[Player.first_name], это не совсем в моем стиле. . ."

    return

label Rogue_black_nipple_tape_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "lipbite")

        ch_Rogue "Хорошо, [Rogue.Player_petname], но она не оставит большого простора для воображения."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "С таким же успехом ты мог бы оставить меня совсем без одежды. . ."

    return

label Rogue_black_nipple_tape_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "lipbite")

        ch_Rogue "Снимать его будет ужасно больно."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "[Rogue.Player_petname!c], ты этого хотел?"

        $ Rogue.eyes = "neutral"

    return

label Rogue_black_nipple_tape_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Только потому, что ты этого хочешь."
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Я начинаю привыкать к тому, что так сильно увлекаю тебя."

    return

label Rogue_black_nipple_tape_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "lipbite")

        ch_Rogue "Снимать его будет ужасно больно."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], ты этого хотел?"

    return
