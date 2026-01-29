define Rogue_all_Clothes["black_gloves"] = {
    "name": "черные перчатки",
    "short_name": "перчатки",
    "short_name_rod": "перчаток",
    "short_name_dat": "перчаткам",
    "short_name_vin": "перчатки",
    "short_name_tvo": "перчатками",
    "short_name_pre": "перчатках",

    "type": "gloves"}

label Rogue_black_gloves_shopping_accept:

    return

label Rogue_black_gloves_shopping_reject:

    return

label Rogue_black_gloves_gift_accept:

    return

label Rogue_black_gloves_gift_reject:

    return

label Rogue_black_gloves_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Как ни странно, они были у меня еще до того, как появились мои способности. . ."
        ch_Rogue "Мой готический стиль пришелся как нельзя кстати."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Я чувствовала себя странно без них."

    return

label Rogue_black_gloves_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Иногда я жалею, что они мне нужны."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ты бы удивился, узнав, сколькими разными способами можно украсить перчатки."

    return

label Rogue_black_gloves_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Забавно, но они были у меня еще до того, как появились мои способности. . ."
        ch_Rogue "Мой готический стиль пришелся как нельзя кстати."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Я чувствовала себя странно без них."

    return

label Rogue_black_gloves_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Иногда я жалею, что они мне нужны."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Я так привыкла носить перчатки, что иногда забываю о них."


    return
