define Rogue_all_Clothes["black_spiked_bracelets"] = {
    "name": _("black spiked bracelets"),
    "short_name": _("spiked bracelets"),

    "type": "sleeves",
    "categories": {
        "bracelets",
        "spiked",
        "accessory",

        "plural",
    },
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("They're kinda part of my signature style at this point.")),

        flags = {"change_Clothing", "black_spiked_bracelets"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah could knock someone out with these.")),

        flags = {"change_Clothing", "black_spiked_bracelets"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah got these after goin' to my first concert.")),

        flags = {"change_Clothing", "black_spiked_bracelets"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("They're one of the oldest things Ah own. . .")),

        flags = {"change_Clothing", "black_spiked_bracelets"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}