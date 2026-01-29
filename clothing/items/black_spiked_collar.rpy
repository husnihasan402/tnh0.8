define Rogue_all_Clothes["black_spiked_collar"] = {
    "name": "черный ошейник с шипами",
    "short_name": "ошейник",
    "short_name_rod": "ошейника",
    "short_name_dat": "ошейнику",
    "short_name_vin": "ошейник",
    "short_name_tvo": "ошейником",
    "short_name_pre": "ошейнике",

    "type": "neck"}

label Rogue_black_spiked_collar_shopping_accept:

    return

label Rogue_black_spiked_collar_shopping_reject:

    return

label Rogue_black_spiked_collar_gift_accept:

    return

label Rogue_black_spiked_collar_gift_reject:

    return

label Rogue_black_spiked_collar_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Сейчас я чувствую, словно он стал частью меня. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Это какой-то фетиш. . ?"

        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Rogue "Пожалуй. . ."

    return

label Rogue_black_spiked_collar_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Никогда раньше не думала, что буду носить что-то подобное. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("devious")

        ch_Rogue "Что тебя так в нем привлекает?"

    return

label Rogue_black_spiked_collar_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Сейчас я чувствую, словно он стал частью меня. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite")

        ch_Rogue "Надеюсь, никто не смотрит."

    return

label Rogue_black_spiked_collar_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Никогда раньше не думала, что буду носить что-то подобное. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я уже почти привыкла к странным взглядам в мою сторону, когда я его ношу."

    return
