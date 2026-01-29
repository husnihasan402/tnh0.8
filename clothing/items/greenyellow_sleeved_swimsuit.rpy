define Rogue_all_Clothes["greenyellow_sleeved_swimsuit"] = {
    "name": "зелено-желтый купальник с рукавами",
    "short_name": "купальник",
    "short_name_rod": "купальника",
    "short_name_dat": "купальнику",
    "short_name_vin": "купальник",
    "short_name_tvo": "купальником",
    "short_name_pre": "купальнике",

    "type": "bodysuit",

    "shame": (0, -50),

    "available_states": {
        "standing": (0, 1, 2, 3)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0, 2),
            "breasts": (0, 2),
            "back": (0, 1, 2, 3),
            "belly": (0, 1, 2, 3),
            "underwear": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},
    "hides": {
        "standing": {
            "breasts": (0, 2),
            "back": (0, 1, 2, 3),
            "belly": (0, 1, 2, 3),
            "pussy": (0, 1),
            "anus": (0, 1)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (0, 1),
            "black_cage_thong": (1,),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "black_tights": (1,),
            "green_bikini_top": (0, 1),
            "green_bikini_bottoms": (1,),
            "green_lace_bra": (0, 1),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        1: {
            "black_cage_bra": (0, 1),
            "black_cage_thong": (1,),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "black_tights": (1,),
            "green_bikini_top": (0, 1),
            "green_bikini_bottoms": (1,),
            "green_lace_bra": (0, 1),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        2: {
            "black_cage_bra": (0, 1),
            "black_cage_thong": (1,),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "black_tights": (1,),
            "green_bikini_top": (0, 1),
            "green_bikini_bottoms": (1,),
            "green_lace_bra": (0, 1),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        3: {
            "black_cage_bra": (0, 1),
            "black_cage_thong": (1,),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "black_tights": (1,),
            "green_bikini_top": (0, 1),
            "green_bikini_bottoms": (1,),
            "green_lace_bra": (0, 1),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},

        "take_off": {
            "black_jeans": (0, 1, 2),
            "black_leather_skirt": (0, 1),
            "black_spiked_bracelets": (0,),
            "brown_utility_belt": (0,),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1)}},
    "covered_by": {
        0: {
            "black_jeans": (0,)},
        1: {
            "black_jeans": (0,)},
        2: {
            "black_jeans": (0,)},
        3: {
            "black_jeans": (0,)}}}

label Rogue_greenyellow_sleeved_swimsuit_shopping_accept:

    return

label Rogue_greenyellow_sleeved_swimsuit_shopping_reject:

    return

label Rogue_greenyellow_sleeved_swimsuit_gift_accept:

    return

label Rogue_greenyellow_sleeved_swimsuit_gift_reject:

    return

label Rogue_greenyellow_sleeved_swimsuit_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь сводить меня искупаться?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], я бы не отказалась поплавать."

    return

label Rogue_greenyellow_sleeved_swimsuit_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], лови волну."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        if approval_check(Rogue, threshold = "sexual_flirting"):
            ch_Rogue "По правде говоря, я так усердно тренировалась, чтобы научиться контролировать свои способности, что могу надевать и снимать купальник за считанные секунды."

            $ Rogue.change_face("wink")

        ch_Rogue "Может быть, когда-нибудь мы сможем принять участие в соревнованиях?"

    return

label Rogue_greenyellow_sleeved_swimsuit_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь сводить меня искупаться?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], я бы не отказалась поплавать."

    return

label Rogue_greenyellow_sleeved_swimsuit_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Мне нравится, как выглядит мое тело в этом старом купальнике."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], лови волну."

    return
