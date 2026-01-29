define Rogue_all_Clothes["green_bikini_bottoms"] = {
    "name": "зеленые трусики бикини",
    "short_name": "трусики бикини",
    "short_name_rod": "трусиков бикини",
    "short_name_dat": "трусикам бикини",
    "short_name_vin": "трусики бикини",
    "short_name_tvo": "трусиками бикини",
    "short_name_pre": "трусиках бикини",

    "type": "underwear",
    "chapter": 1,
    "season": 2,

    "price": 2,

    "shame": (0, 75),

    "available_states": {
        "standing": (0, 1)},
    "undressed_states": {
        "standing": 1},

    "covers": {
        "standing": {
            "pussy": (0,),
            "anus": (0,)},
        "doggy": {
            "pussy": (0,),
            "anus": (0,)},
        "hands_and_knees": {
            "pussy": (0,),
            "anus": (0,)},
        "leaning_back": {
            "pussy": (0,),
            "anus": (0,)}},
    "hides": {
        "standing": {
            "pussy": (0,),
            "anus": (0,)},
        "doggy": {
            "pussy": (0,),
            "anus": (0,)},
        "hands_and_knees": {
            "pussy": (0,),
            "anus": (0,)},
        "leaning_back": {
            "pussy": (0,),
            "anus": (0,)}},

    "blocked_by": {
        "take_off": {
            "black_jeans": (0, 1, 2),
            "black_tights": (0, 1),
            "dark_denim_shorts": (0, 1, 2),
            "green_athletic_shorts": (0, 1),
            "green_running_tights": (0, 1),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1, 2, 3)}},
    "obscured_by": {
        0: {
            "black_jeans": (0,),
            "black_leather_skirt": (0,),
            "dark_denim_shorts": (0,),
            "green_athletic_shorts": (0,),
            "green_maxi_dress": (0, 1),
            "green_running_tights": (0,),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}},
    "covered_by": {
        0: {
            "black_jeans": (0, 1),
            "black_leather_skirt": (0,),
            "black_tights": (0,),
            "dark_denim_shorts": (0, 1),
            "green_athletic_shorts": (0,),
            "green_lace_nighty": (0, 1),
            "green_maxi_dress": (0, 1),
            "green_running_tights": (0,),
            "green_sweater_dress": (0,),
            "greenyellow_classic_suit": (0, 1),
            "greenyellow_sleeved_swimsuit": (0, 1),
            "greybrown_plaid_jacket": (1,),
            "towel": (0,),
            "yellow_summer_dress": (0, 1)}}}

label Rogue_green_bikini_bottoms_shopping_accept:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("pleased2")

    ch_Rogue "Это правда мне? Они такие милые. . ."

    return

label Rogue_green_bikini_bottoms_shopping_reject:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("confused1")

    ch_Rogue "Ты правда думал, что я буду не против, если ты подберешь мне трусики бикини. . . ?"

    return

label Rogue_green_bikini_bottoms_gift_accept:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("pleased1")

    ch_Rogue "Ах. . . они. . . очень милые. . ."

    return

label Rogue_green_bikini_bottoms_gift_reject:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("perplexed")

    ch_Rogue "Хочешь подарить мне такие обтягивающие трусики бикини. . . ты серьезно, дорогой?"

    return

label Rogue_green_bikini_bottoms_change_private_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], я бы не отказалась поплавать."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Хочешь поплавать со мной? Или желаешь просто рассмотреть меня получше?"

    return

label Rogue_green_bikini_bottoms_change_private_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Они довольно откровенные. . . но я бы в них поплавала. . ."

        $ Rogue.eyes = "neutral"
    elif dice_roll == 2:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне теперь немного прохладно, но мне нравится, как они сидят на мне. . ."

    return

label Rogue_green_bikini_bottoms_change_public_before:
    if approval_check(Rogue, threshold = "sexual_flirting"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "[Rogue.Player_petname!c], я бы не отказалась поплавать."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Тебе нравится, что они зеленые, или что они откровенные?"

        $ Rogue.change_face("sly")

    return

label Rogue_green_bikini_bottoms_change_public_after:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sly")

        ch_Rogue "Мне теперь немного прохладно, но мне нравится, как они сидят на мне. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy")

        if approval_check(Rogue, threshold = "sexual_flirting"):
            ch_Rogue "По правде говоря, я так много тренировалась, чтобы контролировать свои способности, что могу надеть и снять купальник за несколько секунд."

            $ Rogue.change_face("wink")

        ch_Rogue "Может быть, когда-нибудь мы сможем принять участие в соревнованиях?"

    return
