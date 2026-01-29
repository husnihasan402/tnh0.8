define Rogue_all_Clothes["black_thighhigh_boots"] = {
    "name": "черные сапоги",
    "short_name_rod": "сапог",
    "short_name_dat": "сапогам",
    "short_name_vin": "сапоги",
    "short_name_tvo": "сапогами",
    "short_name_pre": "сапогах",
    "short_name": "сапоги",

    "type": "footwear",

    "shame": (-5, -5),

    "covers": {
        "standing": {
            "feet": (0,)}},
    "hides": {
        "standing": {
            "feet": (0,)}},

    "blocked_by": {
        0: {
            "black_jeans": (2,),
            "black_tights": (1,),
            "dark_denim_shorts": (2,),
            "green_athletic_shorts": (1,),
            "green_running_tights": (1,)}}}

label Rogue_black_thighhigh_boots_shopping_accept:

    return

label Rogue_black_thighhigh_boots_shopping_reject:

    return

label Rogue_black_thighhigh_boots_gift_accept:

    return

label Rogue_black_thighhigh_boots_gift_reject:

    return

label Rogue_black_thighhigh_boots_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Конечно. Только помоги мне их надеть, ладно?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], пытаешься хоть мельком увидеть мои ножки?"
        ch_Rogue "Пожалуй, я могу позволить тебе посмотреть."

    return

label Rogue_black_thighhigh_boots_change_private_after:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне они очень нравятся."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Теперь тебе придется сводить меня в какое-нибудь приличное местечко, чтобы я могла сверкнуть."

    return

label Rogue_black_thighhigh_boots_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Конечно. Только помоги мне их надеть, ладно?"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "[Rogue.Player_petname!c], пытаешься хоть мельком увидеть мои ножки?"
        ch_Rogue "Пожалуй, я могу позволить тебе посмотреть."

    return

label Rogue_black_thighhigh_boots_change_public_after:
    if approval_check(Rogue, threshold = "dating"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Мне они очень нравятся."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Теперь тебе придется сводить меня в какое-нибудь приличное местечко, чтобы я могла сверкнуть."

    return
