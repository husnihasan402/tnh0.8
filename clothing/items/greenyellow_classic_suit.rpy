define Rogue_all_Clothes["greenyellow_classic_suit"] = {
    "name": "классический костюм в зелено-желтых тонах",
    "short_name": "костюм",
    "short_name_rod": "костюма",
    "short_name_dat": "костюму",
    "short_name_vin": "костюм",
    "short_name_tvo": "костюмом",
    "short_name_pre": "костюме",

    "type": "bodysuit",

    "shame": (0, 15),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,),
            "belly": (0,),
            "thighs": (0, 1),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1),
            "feet": (0, 1)}},
    "hides": {
        "standing": {
            "bra": (0,),
            "breasts": (0,),
            "back": (0,),
            "belly": (0,),
            "thighs": (0, 1),
            "underwear": (0, 1),
            "ass": (0, 1),
            "pussy": (0, 1),
            "anus": (0, 1),
            "feet": (0, 1)}},

    "blocked_by": {
        0: {
            "black_cage_bra": (1,),
            "black_cage_thong": (1,),
            "black_keyhole_bra": (1,),
            "black_sports_bra": (1,),
            "black_tanktop": (1,),
            "black_tights": (1,),
            "green_bikini_top": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_bra": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},
        1: {
            "black_cage_thong": (1,),
            "black_tights": (1,),
            "green_bikini_bottoms": (1,),
            "green_lace_panties": (1,),
            "green_running_tights": (1,),
            "green_thong": (1,),
            "greenblack_boyshorts": (1,),
            "yellow_panties": (1,)},

        "take_off": {
            "black_heels": (0,),
            "black_jeans": (0, 1, 2),
            "black_leather_skirt": (0, 1),
            "black_lowcut_top": (0, 1),
            "black_spiked_bracelets": (0,),
            "black_strap_pumps": (0,),
            "black_thighhigh_boots": (0,),
            "blackgreen_sneakers": (0,),
            "brown_classic_jacket": (0, 1),
            "brown_utility_belt": (0,),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_mesh_top": (0, 1),
            "greybrown_plaid_jacket": (1,),
            "towel": (0, 1),
            "yellow_classic_boots": (0,),
            "yellow_gloves": (0,),
            "yellow_summer_dress": (0, 1, 2, 3)}},
    "covered_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "black_lowcut_top": (0,),
            "brown_classic_jacket": (0, 1),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_maxi_dress": (0, 1),
            "green_mesh_top": (0,),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1, 2, 3)}}}

label Rogue_greenyellow_classic_suit_shopping_accept:

    return

label Rogue_greenyellow_classic_suit_shopping_reject:

    return

label Rogue_greenyellow_classic_suit_gift_accept:

    return

label Rogue_greenyellow_classic_suit_gift_reject:

    return

label Rogue_greenyellow_classic_suit_change_private_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне очень нравятся его цвета."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Хочешь увидеть меня в моем старом боевом костюме?"

    return

label Rogue_greenyellow_classic_suit_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Rogue "Он хорошо подчеркивает мою фигуру. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я спроектировала его сама. Нам сказали, что у нас в костюмах должен присутствовать желтый цвет. Мне поначалу этот цвет не нравился, но потом я привыкла."

    return

label Rogue_greenyellow_classic_suit_change_public_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне очень нравятся его цвета."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Хочешь увидеть меня в моем старом боевом костюме? Хочешь немного потренироваться со мной?"

    return

label Rogue_greenyellow_classic_suit_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Rogue "Он хорошо подчеркивает мою фигуру. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Я спроектировала его сама. Нам сказали, что у нас в костюмах должен присутствовать желтый цвет. Мне поначалу этот цвет не нравился, но потом я привыкла."

    return
