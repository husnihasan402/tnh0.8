define Rogue_all_Clothes["black_spiked_collar"] = {
    "name": _("black spiked collar"),
    "short_name": _("collar"),

    "type": "neck",
    "categories": {
        "collar",
        "spiked",
        "accessory",

        "plural",
    },
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("This is startin' to feel like part of me at this point. . .")),

        flags = {"change_Clothing", "black_spiked_collar"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}