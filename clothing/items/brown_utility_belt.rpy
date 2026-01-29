define Rogue_all_Clothes["brown_utility_belt"] = {
    "name": "коричневый пояс",
    "short_name": "пояс",
    "short_name_rod": "пояса",
    "short_name_dat": "поясу",
    "short_name_vin": "пояс",
    "short_name_tvo": "поясом",
    "short_name_pre": "поясе",

    "type": "belt",

    "blocked_by": {
        0: {
            "green_maxi_dress": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3),
            "yellow_summer_dress": (0, 1, 2, 3)}}}

label Rogue_brown_utility_belt_shopping_accept:

    return

label Rogue_brown_utility_belt_shopping_reject:

    return

label Rogue_brown_utility_belt_gift_accept:

    return

label Rogue_brown_utility_belt_gift_reject:

    return

label Rogue_brown_utility_belt_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Почти уверена, что в него можно поместить практически все необходимое."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Иногда, когда я иду потренироваться в Комнату Опасности, я кладу в него фруктовый перекус - больше всего я люблю яблоки."

    return

label Rogue_brown_utility_belt_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Хех, как же здорово, что все нужные вещи под рукой."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Честно говоря, [Rogue.Player_petname], думаю, ему не помешало бы больше подсумков."

    return

label Rogue_brown_utility_belt_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], как думаешь, мне стоит нацепить его, когда пойду в кино? Уверена, что сюда поместился бы полноценный обед из нескольких блюд."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "И куда я положила ключ от своей комнаты. . ."

    return

label Rogue_brown_utility_belt_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Хех, как же здорово, что все нужные вещи под рукой."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "По правде говоря, с ним ходить куда лучше, чем с сумочкой."

    return
