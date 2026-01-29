define Rogue_all_Clothes["green_headband"] = {
    "name": "зеленая повязка на голову",
    "short_name": "повязка на голову",
    "short_name_rod": "повязки на голову",
    "short_name_dat": "повязке на голову",
    "short_name_vin": "повязку на голову",
    "short_name_tvo": "повязкой на голову",
    "short_name_pre": "повязке на голову",

    "type": "face_inner_accessory"}

label Rogue_green_headband_shopping_accept:

    return

label Rogue_green_headband_shopping_reject:

    return

label Rogue_green_headband_gift_accept:

    return

label Rogue_green_headband_gift_reject:

    return

label Rogue_green_headband_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Эта фигня незаменима на поле боя."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1")

        ch_Rogue "Мы идем на тренировку?"

    return

label Rogue_green_headband_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Замечательная вещь."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Не могу передать, сколько раз волосы мешали мне нормально потренироваться в Комнате Опасности, пока я не прикурпила себе подобную штуку."

    return

label Rogue_green_headband_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Мы собираемся побегать?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Однажды во время тренировки я забыла уложить волосы и случайно поставила кому-то синяк под глазом, потому что ничего не видела."
        ch_Rogue "Я чуть не умерла от стыда."

    return

label Rogue_green_headband_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Замечательная вещь."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Разве теперь я не выгляжу так, словно мне место на обложке старой кассеты с записью тренировок?"

    return
