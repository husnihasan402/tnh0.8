define Rogue_all_Clothes["short_straight_bob_wet"] = {
    "name": _("short straight bob (wet)"),
    "short_name": _("hair"),

    "type": "hair",
    "categories": {
        "hair",
        "wet",
    },

    "shop_type": "salon",
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ya like it slicked back, huh?")),

        flags = {"change_Clothing", "short_straight_bob_wet"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Don't know why Ah even bother, looks good slicked back anyway.")),

        flags = {"change_Clothing", "short_straight_bob_wet"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}