define Rogue_all_Clothes["green_lace_nighty"] = {
    "name": "зеленая кружевная ночнушка",
    "short_name": "ночнушка",
    "short_name_rod": "ночнушки",
    "short_name_dat": "ночнушке",
    "short_name_vin": "ночнушку",
    "short_name_tvo": "ночнушкой",
    "short_name_pre": "ночнушке",

    "type": "dress",

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 4,

    "price": 7,

    "shame": (10, 360),

    "available_states": {
        "standing": (0, 1, 2, 3)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0, 2),
            "breasts": (0, 2),
            "back": (0, 1, 2, 3),
            "belly": (0, 1, 2, 3),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1)}},
    "hides": {
        "standing": {
            "breasts": (0, 2)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (0, 1),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "green_bikini_top": (0, 1),
            "green_lace_bra": (0, 1),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        1: {
            "black_cage_bra": (0, 1),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "green_bikini_top": (0, 1),
            "green_lace_bra": (0, 1),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        2: {
            "black_cage_bra": (0, 1),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "green_bikini_top": (0, 1),
            "green_lace_bra": (0, 1),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        3: {
            "black_cage_bra": (0, 1),
            "black_keyhole_bra": (0, 1),
            "black_sports_bra": (0, 1),
            "black_tanktop": (0, 1),
            "green_bikini_top": (0, 1),
            "green_lace_bra": (0, 1),
            "greenyellow_classic_suit": (1,),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},

        "take_off": {
            "black_NIN_shirt": (0, 1),
            "brown_classic_jacket": (0, 1),
            "brown_utility_belt": (0,)}},
    "obscured_by": {
        0: {
            "towel": (0,)},
        1: {
            "towel": (0,)},
        2: {
            "towel": (0,)},
        3: {
            "towel": (0,)}},
    "covered_by": {
        0: {
            "towel": (0, 1)},
        1: {
            "towel": (0, 1)},
        2: {
            "towel": (0, 1)},
        3: {
            "towel": (0, 1)}},

    "traits": {
        "supports_breasts": [0]}}

label Rogue_green_lace_nighty_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Господи, [Rogue.Player_petname], она просто великолепна. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Нечто подобное я видела в каком-то старом слэшере. . ."
    ch_Rogue "Спасибо тебе большое."

    return

label Rogue_green_lace_nighty_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Она очень красивая, [Rogue.Player_petname], но я не хочу, чтобы ты покупал мне нижнее белье."

    $ Rogue.change_face("neutral")

    ch_Rogue "И да, спасибо, что подумал обо мне."

    return

label Rogue_green_lace_nighty_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Это мне? Когда ты успел ее купить?"

    $ Rogue.change_face("sexy")

    ch_Rogue "Спасибо, мне очень нравится."

    return

label Rogue_green_lace_nighty_gift_reject:
    $ Rogue.change_face("confused2")

    ch_Rogue "Извини, [Rogue.Player_petname], надеюсь, ты сохранил чек."
    ch_Rogue "Думаю, тебе не стоило покупать мне кружевную ночнушку, даже если она очень милая."

    return

label Rogue_green_lace_nighty_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Она довольно тоненькая. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk1")

        ch_Rogue"Надеюсь, ты не хочешь просто посмотреть на нее."

    return

label Rogue_green_lace_nighty_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        ch_Rogue "Я чувствую себя в ней принцессой."
    elif dice_roll == 2:
        $ Rogue.change_face("wink")

        ch_Rogue "Надеюсь, мы найдем время для того, чтобы немного поваляться."

    return

label Rogue_green_lace_nighty_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Смелый выбор, [Rogue.Player_petname]. Мне нравится."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Не мог дождаться, когда вернемся в одну из наших комнат?"

    return

label Rogue_green_lace_nighty_change_public_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "В ней немного прохладно, [Rogue.Player_petname]."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Не уверена, что привыкла к повышенному вниманию, но выражение твоего лица того стоит."

    return
