define Rogue_all_Clothes["black_tanktop"] = {
    "name": "черная майка",
    "short_name": "майка",
    "short_name_rod": "майки",
    "short_name_dat": "майке",
    "short_name_vin": "майку",
    "short_name_tvo": "майкой",
    "short_name_pre": "майке",

    "type": "bra",

    "shame": (0, 15),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "breasts": (0,)},
        "doggy": {
            "breasts": (0,)},
        "hands_and_knees": {
            "breasts": (0,)},
        "leaning_back": {
            "breasts": (0,)}},
    "hides": {
        "standing": {
            "breasts": (0,)},
        "doggy": {
            "breasts": (0,)},
        "hands_and_knees": {
            "breasts": (0,)},
        "leaning_back": {
            "breasts": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_fishnet_top": (0, 1),
            "black_lowcut_top": (0, 1),
            "black_NIN_shirt": (0, 1),
            "brown_classic_jacket": (0, 1),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0, 1),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},
    "obscured_by": {
        0: {
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "green_maxi_dress": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}},
    "covered_by": {
        0: {
            "black_fishnet_top": (0,),
            "black_lowcut_top": (0,),
            "black_NIN_shirt": (0,),
            "brown_classic_jacket": (0,),
            "green_maxi_dress": (0,),
            "green_mesh_top": (0,),
            "green_sweater_dress": (0, 2),
            "greenyellow_classic_suit": (0,),
            "yellow_summer_dress": (0, 2)}}}

label Rogue_black_tanktop_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Я раньше носила нечто подобное. . ."

    return

label Rogue_black_tanktop_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Мне она ни к чему, большое спасибо."

    return

label Rogue_black_tanktop_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Где ты ее нашел?"

    $ Rogue.change_face("pleased1")

    ch_Rogue "У меня был точно такой же в школе. . ."

    return

label Rogue_black_tanktop_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Эм. . . нет, спасибо, дорогой."

    return

label Rogue_black_tanktop_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Такая же майка была первой вещью, которую я купила, прибыв сюда."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я не против показать тебе немного своего тела."

    return

label Rogue_black_tanktop_change_private_after:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", eyes = "down")

        ch_Rogue "Выглядит точно так же, как я помню. . ."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        ch_Rogue "Если захочешь заглянуть под нее, только попроси."

    return

label Rogue_black_tanktop_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Такая же майка была первой вещью, которую я купила, прибыв сюда."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Лучше даже не пытайся увидеть мою грудь."

    return

label Rogue_black_tanktop_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ах, такая удобная."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Я никогда не осознавала, насколько откровенной может быть эта майка."

    return
