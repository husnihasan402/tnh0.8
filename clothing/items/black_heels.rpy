define Rogue_all_Clothes["black_heels"] = {
    "name": "черные туфли",
    "short_name": "туфли",
    "short_name_rod": "туфель",
    "short_name_dat": "туфлям",
    "short_name_vin": "туфли",
    "short_name_tvo": "туфлями",
    "short_name_pre": "туфлях",

    "type": "footwear",

    "chapter": 1,
    "season": 4,

    "price": 5,

    "shame": (5, 10),

    "covers": {
        "standing": {
            "feet": (0,)}}}

label Rogue_black_heels_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Они идеально подходят для свиданий!"

    if Rogue in Partners:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Если мы пойдем в какое-нибудь по-настоящему модное место. . ."
        ch_Rogue "То мне стоит надеть их, если ты, конечно, захочешь."

    return

label Rogue_black_heels_shopping_reject:
    $ Rogue.change_face("appalled2")

    ch_Rogue "Хочешь подарить мне туфли для стриптиза?"
    ch_Rogue "Ты, должно быть, сошел с ума."

    return

label Rogue_black_heels_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Они идеально подходят для свиданий!"

    if Rogue in Partners:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Если мы пойдем в какое-нибудь по-настоящему модное место. . ."
        ch_Rogue "То мне стоит надеть их, если ты, конечно, захочешь."

    return

label Rogue_black_heels_gift_reject:
    $ Rogue.change_face("appalled2")

    ch_Rogue "Хочешь подарить мне туфли для стриптиза?"
    ch_Rogue "Ты, должно быть, сошел с ума."

    return

label Rogue_black_heels_change_private_before:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Надеть их и никуда не пойти? Любопытно. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Ты хочешь пригласить меня в какое-то модное место или тебе просто нравятся каблуки?"

    return

label Rogue_black_heels_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], я бы с удовольствием прогулялась по городу сегодня вечером в этих туфлях."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Даже на каблуках я все равно ниже тебя."

    return

label Rogue_black_heels_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "[Rogue.Player_petname!c], ты уверен, что хочешь отказаться от своего преимущества в росте?"
        ch_Rogue "Ну. . . Даже на каблуках до тебя мне все равно далеко, но. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Пора показать себя во всей красе."

        if Rogue in Partners:
            $ Rogue.change_face("sly")

            ch_Rogue "Тебе лучше не отводить от меня взгляда."

    return

label Rogue_black_heels_change_public_after:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "[Rogue.Player_petname!c], может сходим сегодня в город?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        ch_Rogue "Если ты собираешься пригласить меня куда-нибудь, нам лучше идти сейчас, потому что ходить на каблуках - это настоящая мука."

    return
