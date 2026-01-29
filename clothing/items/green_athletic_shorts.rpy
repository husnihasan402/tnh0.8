define Rogue_all_Clothes["green_athletic_shorts"] = {
    "name": "зеленые спортивные шорты",
    "short_name": "шорты",
    "short_name_rod": "шорт",
    "short_name_dat": "шортам",
    "short_name_vin": "шорты",
    "short_name_tvo": "шортами",
    "short_name_pre": "шортах",

    "type": "pants",
    "chapter": 1,
    "season": 1,

    "price": 4,

    "shame": (-5, 10),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        0: {
            "black_cage_thong": (1,),
            "black_tights": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)}},
    "obscured_by": {
        0: {
            "black_leather_skirt": (0,),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}},
    "covered_by": {
        0: {
            "black_leather_skirt": (0,),
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_green_athletic_shorts_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Хм, хороший выбор, выглядят удобными."

    return

label Rogue_green_athletic_shorts_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Я могу сама выбрать себе одежду, спасибо."

    return

label Rogue_green_athletic_shorts_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Они выглядят удобными. . ."

    return

label Rogue_green_athletic_shorts_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Я могу сама купить себе шорты, спасибо."

    return

label Rogue_green_athletic_shorts_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Хочешь потренироваться?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Желаешь потренироваться вместе или хочешь просто хорошенько рассмотреть мою попку?"

    return

label Rogue_green_athletic_shorts_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Они не {i}слишком{/i} короткие?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Если хочешь, я могу повернуться."

    return

label Rogue_green_athletic_shorts_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я знаю, что тебе нравится, когда я в них."

    return

label Rogue_green_athletic_shorts_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Они удобные."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Возможно, позже мы сможем потренироваться наедине."

    return
