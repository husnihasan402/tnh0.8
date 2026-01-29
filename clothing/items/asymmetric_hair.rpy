define Rogue_all_Clothes["asymmetric"] = {
    "name": "асимметричная прическа",
    "short_name": "hair",

    "type": "hair",

    "shop_type": "salon",

    "available_states": {
        "standing": (0,),
        "doggy": (0,),
        "hands_and_knees": (0,),
        "leaning_back": (0,),
        "missionary": (0,)},
    "undressed_states": {
        "standing": 0,
        "doggy": 0,
        "hands_and_knees": 0,
        "leaning_back": 0,
        "missionary": 0}}

label Rogue_asymmetric_hair_shopping_accept:

    return

label Rogue_asymmetric_hair_shopping_reject:

    return

label Rogue_asymmetric_hair_gift_accept:

    return

label Rogue_asymmetric_hair_gift_reject:

    return

label Rogue_asymmetric_hair_change_private_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2")
        $ Rogue.change_arms("hips", right_arm = "neutral")

        ch_Rogue "Мне кажется, без этой прически я не похожа на саму себя."

        $ Rogue.change_face("worried1", mouth = "smirk")
        $ Rogue.change_arms("crossed")

        ch_Rogue "С ней я чувствую, что могу привыкнуть к тому, что нахожусь здесь и занимаюсь всем этим."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")
        $ Rogue.change_arms("sass")

        ch_Rogue "Конечно, дай мне только найти свою расческу."
    elif dice_roll == 3:
        $ Rogue.change_face("confused1")
        $ Rogue.change_arms("sheepish", left_arm = "rub_neck")

        ch_Rogue "Похоже, тебе нравится эта прическа. . ."

    return

label Rogue_asymmetric_hair_change_private_after:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "smirk")
        $ Rogue.change_arms("sheepish")

        ch_Rogue "На то, чтобы сделать пробор в первый раз, ушла целая вечность."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")
        $ Rogue.change_arms("neutral")

        ch_Rogue "Ну вот, [Rogue.Player_petname]."
        ch_Rogue "Разве это не классика?"
    elif dice_roll == 3:
        $ Rogue.change_face("pleased1")
        $ Rogue.change_arms("hips")

        ch_Rogue "Думаю, она мне идет."

    return

label Rogue_asymmetric_hair_change_public_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")
        $ Rogue.change_arms("shrug")

        ch_Rogue "Хорошо, что прихватила расческу."
    elif dice_roll == 2:
        $ Rogue.change_face("sly")
        $ Rogue.change_arms("crossed")

        ch_Rogue "Это не так просто, как кажется."
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")
        $ Rogue.change_arms("sheepish", right_arm = "extended")

        ch_Rogue "Эм, здесь. . . ?"

    return

label Rogue_asymmetric_hair_change_public_after:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", mouth = "smirk")
        $ Rogue.change_arms("sheepish")

        ch_Rogue "Нравится?"
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")
        $ Rogue.change_arms("hips", right_arm = "neutral")

        ch_Rogue "Мне кажется, без этой прически я не похожа на саму себя."
    elif dice_roll == 3:
        $ Rogue.change_face("smirk1")
        $ Rogue.change_arms("sass")

        ch_Rogue "Надеюсь, у меня нормально получилось. . ."

    return
