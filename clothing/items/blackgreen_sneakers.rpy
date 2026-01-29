define Rogue_all_Clothes["blackgreen_sneakers"] = {
    "name": "черно-зеленые кроссовки",
    "short_name": "кроссовки",
    "short_name_rod": "кроссовок",
    "short_name_dat": "кроссовкам",
    "short_name_vin": "кроссовки",
    "short_name_tvo": "кроссовками",
    "short_name_pre": "кроссовках",

    "type": "footwear",

    "covers": {
        "standing": {
            "feet": (0,)}},
    "hides": {
        "standing": {
            "feet": (0,)}}}

label Rogue_blackgreen_sneakers_shopping_accept:

    return

label Rogue_blackgreen_sneakers_shopping_reject:

    return

label Rogue_blackgreen_sneakers_gift_accept:

    return

label Rogue_blackgreen_sneakers_gift_reject:

    return

label Rogue_blackgreen_sneakers_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Мы собираемся на тренировку?"
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Профессору Икс следует повысить нам стипендию, чтобы мы не разорились, покупая новые кроссовки каждые несколько месяцев."

    return

label Rogue_blackgreen_sneakers_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("wink")

        ch_Rogue "Может, как-нибудь нам стоит побегать?"
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Они намного удобнее моих ботинок."

    return

label Rogue_blackgreen_sneakers_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Я бы с удовольствием как-нибудь сходила в поход."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Они очень удобные."

    return

label Rogue_blackgreen_sneakers_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("wink")

        ch_Rogue "Может, как-нибудь нам стоит побегать?"
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Они намного удобнее моих ботинок."

    return
