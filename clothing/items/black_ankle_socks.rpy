define Rogue_all_Clothes["black_ankle_socks"] = {
    "name": "черные носки",
    "short_name": "носки",
    "short_name_rod": "носков",
    "short_name_dat": "носкам",
    "short_name_vin": "носки",
    "short_name_tvo": "носками",
    "short_name_dat": "носках",

    "type": "socks",

    "covers": {
        "standing": {
            "feet": (0,)}},
    "hides": {
        "standing": {
            "feet": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_heels": (0,),
            "black_strap_pumps": (0,),
            "black_thighhigh_boots": (0,),
            "blackgreen_sneakers": (0,),
            "greenyellow_classic_suit": (0,),
            "yellow_classic_boots": (0,)}},
    "obscured_by": {
        0: {
            "black_thighhigh_boots": (0,),
            "blackgreen_sneakers": (0,),
            "greenyellow_classic_suit": (0,),
            "yellow_classic_boots": (0,)}},
    "covered_by": {
        0: {
            "black_heels": (0,),
            "black_strap_pumps": (0,),
            "black_thighhigh_boots": (0,),
            "blackgreen_sneakers": (0,),
            "greenyellow_classic_suit": (0,),
            "yellow_classic_boots": (0,)}}}

label Rogue_black_ankle_socks_shopping_accept:

    return

label Rogue_black_ankle_socks_shopping_reject:

    return

label Rogue_black_ankle_socks_gift_accept:

    return

label Rogue_black_ankle_socks_gift_reject:

    return

label Rogue_black_ankle_socks_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Уверена, у меня есть почти все части одежды черного цвета."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "До прибытия сюда у меня не было обычных носков."

    return

label Rogue_black_ankle_socks_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я вообще не чувствую, что они на мне!"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне все еще тяжело привыкнуть, что они такие короткие. . ."

    return

label Rogue_black_ankle_socks_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Эти носки идеально сочетаются с моими кроссовками для бега."

        if EventScheduler.check("Rogue_chapter_one_season_one_jogging"):
            ch_Rogue "И я очень рада, что мне наконец-то есть с кем побегать."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "До прибытия у меня не было обычных носков."

    return

label Rogue_black_ankle_socks_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Я вообще не чувствую, что они на мне."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне все еще тяжело привыкнуть, что они такие короткие. . ."

    return
