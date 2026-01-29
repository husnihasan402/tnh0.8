define Rogue_all_Clothes["greybrown_plaid_jacket"] = {
    "name": "серо-коричневый клетчатый пиджак",
    "short_name": "пиджак",
    "short_name_rod": "пиджака",
    "short_name_dat": "пиджаку",
    "short_name_vin": "пиджак",
    "short_name_tvo": "пиджаком",
    "short_name_pre": "пиджаке",

    "type": "jacket",

    "shame": (-30, -30),

    "available_states": {
        "standing": (1,)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (1,),
            "breasts": (1,),
            "back": (1,),
            "belly": (1,)}},
    "hides": {
        "standing": {
            "breasts": (1,),
            "back": (1,)}},

    "blocked_by": {
        1: {
            "black_lowcut_top": (0, 1),
            "green_lace_nighty": (0, 1, 2, 3),
            "green_maxi_dress": (0, 1),
            "green_mesh_top": (0, 1),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "towel": (0, 1)}}}

label Rogue_greybrown_plaid_jacket_shopping_accept:

    return

label Rogue_greybrown_plaid_jacket_shopping_reject:

    return

label Rogue_greybrown_plaid_jacket_gift_accept:

    return

label Rogue_greybrown_plaid_jacket_gift_reject:

    return

label Rogue_greybrown_plaid_jacket_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1")

            ch_Rogue "Хочешь, чтобы я надела больше одежды?"
        elif dice_roll == 2:
            $ Rogue.change_face("confused1")

            ch_Rogue "Никогда не думала, что ты захочешь, чтобы я надела больше одежды."

    return

label Rogue_greybrown_plaid_jacket_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Он не в моем обычном стиле, но думаю, в нем я выгляжу мило."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "У него есть подкладка, теперь я не замерзну."

    return

label Rogue_greybrown_plaid_jacket_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1")

            ch_Rogue "Хочешь, чтобы я надела больше одежды?"
        elif dice_roll == 2:
            $ Rogue.change_face("confused1")

            ch_Rogue "Никогда не думала, что ты захочешь, чтобы я надела больше одежды."

    return

label Rogue_greybrown_plaid_jacket_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Он не в моем обычном стиле, но думаю, в нем я выгляжу мило."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "У него есть подкладка, теперь я не замерзну."

    return
