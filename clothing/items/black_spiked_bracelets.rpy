define Rogue_all_Clothes["black_spiked_bracelets"] = {
    "name": "черные браслеты с шипами",
    "short_name": "браслеты с шипами",
    "short_name_rod": "браслетов с шипами",
    "short_name_dat": "браслетам с шипами",
    "short_name_vin": "браслеты с шипами",
    "short_name_tvo": "браслетами с шипами",
    "short_name_pre": "браслетах с шипами",

    "type": "sleeves",

    "blocked_by": {
        0: {
            "black_lowcut_top": (0, 1),
            "yellow_gloves": (0,)}}}

label Rogue_black_spiked_bracelets_shopping_accept:

    return

label Rogue_black_spiked_bracelets_shopping_reject:

    return

label Rogue_black_spiked_bracelets_gift_accept:

    return

label Rogue_black_spiked_bracelets_gift_reject:

    return

label Rogue_black_spiked_bracelets_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "[Rogue.Player_petname!c], нам надо как-нибудь сходить на концерт."
        ch_Rogue "С ними я отлично туда впишусь."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "С ними я выгляжу круто?"

    return

label Rogue_black_spiked_bracelets_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Они очень стильные."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я купила их после того, как сходила на свой первый концерт."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

        ch_Rogue "Они одни из самых старых вещей, которые у меня есть. . ."

    return

label Rogue_black_spiked_bracelets_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Сейчас они вроде как часть моего фирменного стиля."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Ими можно кого-нибудь вырубить."

    return

label Rogue_black_spiked_bracelets_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Они очень стильные."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я купила их после того, как сходила на свой первый концерт."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

        ch_Rogue "Они одни из самых старых вещей, которые у меня есть. . ."

    return
