define Rogue_all_Clothes["black_jeans"] = {
    "name": "черные джинсы",
    "short_name": "джинсы",
    "short_name_rod": "джинсов",
    "short_name_dat": "джинсам",
    "short_name_vin": "джинсы",
    "short_name_tvo": "джинсами",
    "short_name_pre": "джинсах",

    "type": "pants",

    "shame": (-10, -10),

    "available_states": {
        "standing": (0, 1, 2)},
    "undressed_states": {
        "standing": 2},

    "covers": {
        "standing": {
            "thighs": (0, 1),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},
    "hides": {
        "standing": {
            "thighs": (0, 1),
            "underwear": (0,),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},

    "blocked_by": {
        0: {
            "black_cage_thong": (1,),
            "black_tights": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        1: {
            "black_cage_thong": (1,),
            "black_tights": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)}},
    "covered_by": {
        0: {
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_sweater_dress": (0,),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_black_jeans_shopping_accept:

    return

label Rogue_black_jeans_shopping_reject:

    return

label Rogue_black_jeans_gift_accept:

    return

label Rogue_black_jeans_gift_reject:

    return

label Rogue_black_jeans_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Сейчас надену. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я удивлена, что ты хочешь, чтобы я прикрылась."

    return

label Rogue_black_jeans_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Сзади они немного жмут. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Разве они не красивые?"
        ch_Rogue "Я вижу, как ты пялишься на мою попку. . ."

    return

label Rogue_black_jeans_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я удивлена, что ты хочешь, чтобы я прикрылась."

    return

label Rogue_black_jeans_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Сзади они немного жмут. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "В этих джинсах моя попка выглядит нормально?"

    return
