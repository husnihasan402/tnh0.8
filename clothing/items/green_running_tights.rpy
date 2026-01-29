define Rogue_all_Clothes["green_running_tights"] = {
    "name": "зеленые леггинсы для бега",
    "short_name": "леггинсы",
    "short_name_rod": "леггинсов",
    "short_name_dat": "леггинсам",
    "short_name_vin": "леггинсы",
    "short_name_tvo": "леггинсами",
    "short_name_pre": "леггинсах",

    "type": "hose",

    "shame": (-20, -20),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "thighs": (0,),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "thighs": (0,),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        0: {
            "black_cage_thong": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},

        "take_off": {
            "black_jeans": (0, 1, 2),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1),
            "greenyellow_classic_suit": (0, 1)}},
    "obscured_by": {
        0: {
            "black_jeans": (0,),
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

label Rogue_green_running_tights_shopping_accept:

    return

label Rogue_green_running_tights_shopping_reject:

    return

label Rogue_green_running_tights_gift_accept:

    return

label Rogue_green_running_tights_gift_reject:

    return

label Rogue_green_running_tights_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мы собираемся на пробежку?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."

    return

label Rogue_green_running_tights_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Разве в них моя попка выглядит не великолепно?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Возможно, позже мы сможем потренироваться наедине."

    return

label Rogue_green_running_tights_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Иногда я надеваю их, чтобы просто поваляться в комнате, они такие удобные."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."

    return

label Rogue_green_running_tights_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Разве в них моя попка выглядит не великолепно?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Возможно, позже мы сможем потренироваться наедине."

    return
