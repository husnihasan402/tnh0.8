define Rogue_all_Clothes["short_straight_bob_asymmetric"] = {
    "name": _("short straight bob (asymmetric)"),
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
        DialogueClass("ch_Rogue", _("Ah don't think Ah was really myself until Ah got this cut.")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("It was the first thing that made me feel like Ah could get used to bein' out here doin' all this.")),
        ),

        flags = {"change_Clothing", "after", "short_straight_bob_asymmetric"},

        initial = "optional",

        tags = "flavor",
    ),
}