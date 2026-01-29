define Rogue_all_Clothes["green_sweater_dress"] = {
    "name": _("green sweater dress"),
    "short_name": _("dress"),

    "type": "dress",
    "categories": {
        "dress",
        "sweater_dress",
        "booby",
        "comfy",

        "singular",
    },

    "shame": (-5, -5),

    "covers": {
        "standing": {
            "bra": {0, 2},
            "breast": {0, 2},
            "back": {0, 2},
            "belly": {0, 2},
            "underwear": {0},
            "ass": {0},
            "pussy": {0},
            "anus": {0},
        },
    },
    "hides": {
        "standing": {
            "bra": {0, 2},
            "breast": {0, 2},
            "back": {0, 2},
            "belly": {0, 2},
            "underwear": {0},
            "ass": {0},
            "pussy": {0},
            "anus": {0},
        },
    },
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("It's a miracle what you can find out here. . .")),

        flags = {"change_Clothing", "green_sweater_dress"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Nobody'd wear something like this back home.")),

        flags = {"change_Clothing", "green_sweater_dress"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}