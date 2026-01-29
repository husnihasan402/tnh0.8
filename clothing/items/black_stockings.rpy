define Rogue_all_Clothes["black_stockings"] = {
    "name": "черные чулки",
    "short_name": "чулки",
    "short_name_rod": "чулков",
    "short_name_dat": "чулкам",
    "short_name_vin": "чулки",
    "short_name_tvo": "чулками",
    "short_name_pre": "чулках",

    "type": "socks",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 3,

    "shame": (35, 125),

    "covers": {
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
            "black_jeans": (0, 1),
            "greenyellow_classic_suit": (0,)}},
    "covered_by": {
        0: {
            "black_heels": (0,),
            "black_jeans": (0, 1),
            "black_strap_pumps": (0,),
            "black_thighhigh_boots": (0,),
            "blackgreen_sneakers": (0,),
            "greenyellow_classic_suit": (0,),
            "yellow_classic_boots": (0,)}}}

label Rogue_black_stockings_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Боже мой. . ."
    ch_Rogue "Они прекрасны."

    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ Rogue.change_face("sly")

        ch_Rogue "Постарайся не порвать их. . ."

    return

label Rogue_black_stockings_shopping_reject:
    $ Rogue.change_face("worried2")

    ch_Rogue "Я ценю твое предложение, но нет, спасибо."

    return

label Rogue_black_stockings_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Это мне?"
    ch_Rogue "Похоже, ты правильно подобрал мой размер."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Спасибо, [Rogue.Player_petname]."

    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ Rogue.change_face("sly")

        ch_Rogue "Постарайся не порвать их. . ."

    return

label Rogue_black_stockings_gift_reject:
    $ Rogue.change_face("appalled1")

    ch_Rogue "Тебе не стоит волноваться о том, какое нижнее белье мне нужно, а какое - нет."

    return

label Rogue_black_stockings_change_private_before:
    if approval_check(Rogue, threshold = "dating"):
        if approval_check(Rogue, threshold = "sexual_flirting"):
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("sly")

            ch_Rogue "Мы куда-то идем сегодня вечером?"
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Лучше не ограничиваться только ими. . ."

    return

label Rogue_black_stockings_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Я теперь выгляжу как какая-то секретарша."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Тебя они заводят?"

    return

label Rogue_black_stockings_change_public_before:
    if approval_check(Rogue, threshold = "dating"):
        if approval_check(Rogue, threshold = "sexual_flirting"):
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("sexy")

            ch_Rogue "Ты должен сводить меня в какое-нибудь модное заведение, я не хочу наряжаться просто так."
        elif dice_roll == 2:
            $ Rogue.change_face("sly")

            ch_Rogue "Лучше не ограничиваться только ими. . ."

    return

label Rogue_black_stockings_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("confused1")

        ch_Rogue "Клянусь, если мне придется в них бегать, кто-нибудь пострадает."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Тебя они заводят?"

    return
