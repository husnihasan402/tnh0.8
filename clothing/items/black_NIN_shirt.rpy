define Rogue_all_Clothes["black_NIN_shirt"] = {
    "name": "черная футболка NIN",
    "short_name": "футболка",
    "short_name_rod": "футболки",
    "short_name_dat": "футболке",
    "short_name_vin": "футболку",
    "short_name_tvo": "футболкой",
    "short_name_pre": "футболке",

    "type": "jacket",

    "shame": (-10, -5),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,)}},
    "hides": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (1,),
            "black_keyhole_bra": (1,),
            "black_lowcut_top": (0, 1),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "green_bikini_top": (1,),
            "green_lace_bra": (1,),
            "green_lace_nighty": (1,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)},
        1: {
            "black_lowcut_top": (0, 1),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)}}}

label Rogue_black_NIN_shirt_shopping_accept:

    return

label Rogue_black_NIN_shirt_shopping_reject:

    return

label Rogue_black_NIN_shirt_gift_accept:

    return

label Rogue_black_NIN_shirt_gift_reject:

    return

label Rogue_black_NIN_shirt_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "О, вспомнила, я должна составить тебе плейлист своих любимых песен."
        ch_Rogue "И я бы с удовольствием послушала то, что слушаешь ты."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне не нужно повторять дважды."

    return

label Rogue_black_NIN_shirt_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("angry1")

        ch_Rogue "Меня часто спрашивают, зачем я хожу с огромным лого на груди."
        ch_Rogue "Мне жали их, не знают, до чего еще можно докопаться."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я была бы рада, если бы в торговом центре был музыкальный магазин, мы могли бы устроить там классное свидание."

    return

label Rogue_black_NIN_shirt_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "О, вспомнила, я должна составить тебе плейлист своих любимых песен."
        ch_Rogue "И я бы с удовольствием послушала то, что слушаешь ты."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Может, когда-нибудь нам удастся попасть на их концерт? Уверена, тебе понравится."

    return

label Rogue_black_NIN_shirt_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("angry1")

        ch_Rogue "Надеюсь, если мы будем вместе, меня больше не будут спрашивать, зачем я хожу с огромным лого на груди."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я была бы рада, если бы в торговом центре был музыкальный магазин, мы могли бы устроить там классное свидание."

    return
