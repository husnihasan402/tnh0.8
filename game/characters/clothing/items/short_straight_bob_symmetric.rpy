define Rogue_all_Clothes["short_straight_bob_symmetric"] = {
    "name": _("short straight bob (symmetric)"),
    "short_name": _("hair"),

    "type": "hair",
    "categories": {
        "hair",
        "straight",
    },

    "shop_type": "salon",
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ain't it a classic?")),

        flags = {"change_Clothing", "short_straight_bob_symmetric"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}