define Rogue_all_Clothes["green_sweater_dress"] = {
    "name": "зеленое платье-свитер",
    "short_name_rod": "платья",
    "short_name_dat": "платью",
    "short_name_vin": "платье",
    "short_name_tvo": "платьем",
    "short_name_pre": "платье",
    "short_name": "платье",

    "type": "dress",

    "shame": (-5, -5),

    "available_states": {
            "standing": (0, 2)},
    "undressed_states": {
            "standing": 2},

    "covers": {
        "standing": {
            "bra": (0, 2),
            "breasts": (0, 2),
            "back": (0, 2),
            "belly": (0, 2),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "bra": (0, 2),
            "breasts": (0, 2),
            "back": (0, 2),
            "belly": (0, 2),
            "underwear": (0,),
            "ass": (0,),
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (1,),
            "black_keyhole_bra": (1,),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "green_bikini_top": (1,),
            "green_lace_bra": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        2: {
            "black_cage_bra": (1,),
            "black_keyhole_bra": (1,),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "green_bikini_top": (1,),
            "green_lace_bra": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},

        "take_off": {
            "brown_utility_belt": (0,),
            "greybrown_plaid_jacket": (1,)}},
    "covered_by": {
        0: {
            "greybrown_plaid_jacket": (1,)},
        2: {
            "greybrown_plaid_jacket": (1,)}}}

label Rogue_green_sweater_dress_shopping_accept:

    return

label Rogue_green_sweater_dress_shopping_reject:

    return

label Rogue_green_sweater_dress_gift_accept:

    return

label Rogue_green_sweater_dress_gift_reject:

    return

label Rogue_green_sweater_dress_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Я просто обожаю его, оно такое красивое и удобное."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."

    return

label Rogue_green_sweater_dress_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Тебе не кажется, что оно мне очень идет?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Разве в нем моя грудь выглядит не потрясающе?"

    return

label Rogue_green_sweater_dress_change_public_before:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Конечно, [Rogue.Player_petname], сейчас надену."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Я должна надеть его в следующий раз, когда мы пойдем на свидание."

    return

label Rogue_green_sweater_dress_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Тебе не кажется, что оно мне очень идет?"
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Разве оно не милое?"

        $ Rogue.change_face("smirk2")

        ch_Rogue "У меня на родине никто не стал бы носить ничего подобного."

    return
