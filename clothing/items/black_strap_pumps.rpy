define Rogue_all_Clothes["black_strap_pumps"] = {
    "name": "черные туфли с ремешком",
    "short_name": "туфли",
    "short_name_rod": "туфель",
    "short_name_dat": "туфлям",
    "short_name_vin": "туфли",
    "short_name_tvo": "туфлями",
    "short_name_pre": "туфлях",

    "type": "footwear",

    "shame": (5, 10),

    "covers": {
        "standing": {
            "feet": (0,)}}}

label Rogue_black_strap_pumps_shopping_accept:

    return

label Rogue_black_strap_pumps_shopping_reject:

    return

label Rogue_black_strap_pumps_gift_accept:

    return

label Rogue_black_strap_pumps_gift_reject:

    return

label Rogue_black_strap_pumps_change_private_before:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], разве они не сексуальные?"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], сегодня вечером я бы с удовольствием прогулялась с тобой по городу в них."

    return

label Rogue_black_strap_pumps_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased1", eyes = "down")

        pause 1.0

        $ Rogue.eyes = "neutral"

        ch_Rogue "Очень милые, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне так нравится ходить в них."

    return

label Rogue_black_strap_pumps_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], разве они не сексуальные?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мы идем в какое-то хорошее заведение?"

    return

label Rogue_black_strap_pumps_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased1", eyes = "down")

        pause 1.0

        $ Rogue.eyes = "neutral"

        ch_Rogue "Очень милые, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне так нравится ходить в них."

    return
