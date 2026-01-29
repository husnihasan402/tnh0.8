define Rogue_all_Clothes["yellow_gloves"] = {
    "name": "желтые перчатки",
    "short_name": "перчатки",
    "short_name_rod": "перчаток",
    "short_name_dat": "перчаткам",
    "short_name_vin": "перчатки",
    "short_name_tvo": "перчатками",
    "short_name_pre": "перчатках",

    "type": "gloves"}

label Rogue_yellow_gloves_shopping_accept:

    return

label Rogue_yellow_gloves_shopping_reject:

    return

label Rogue_yellow_gloves_gift_accept:

    return

label Rogue_yellow_gloves_gift_reject:

    return

label Rogue_yellow_gloves_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Они клевые, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Ох, мне бы не помешало сменить цвет."

    return

label Rogue_yellow_gloves_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Тебе нравится, как желтый цвет сочетается со мной, да?"
        ch_Rogue "Ты бы удивился, узнав, сколькими разными способами можно украсить перчатки."
    elif dice_roll == 2:
        $ Rogue.change_face("sly", blush = 1)

        ch_Rogue "Мне кажется, у моей силы есть все-таки свои преимущества."

    return

label Rogue_yellow_gloves_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Они клевые, правда?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Это, конечно, не мои повседневные перчатки, но я не против их носить."

    return

label Rogue_yellow_gloves_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "В хороших перчатках всегда чувствуешь себя лучше. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Тебе нравится, как желтый цвет сочетается со мной, да?"
        ch_Rogue "Ты бы удивился, узнав, сколькими разными способами можно украсить перчатки."

    return
