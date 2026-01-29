define Rogue_all_Clothes["greenyellow_sleeved_swimsuit"] = {
    "name": _("green-and-yellow sleeved swimsuit"),
    "short_name": _("swimsuit"),

    "type": "bodysuit",
    "categories": {
        "swimsuit",
        "one_piece",
        "booby",

        "singular",
    },

    "shame": (0, -50),

    "covers": {
        "standing": {
            "bra": {0, 2},
            "breast": {0, 2},
            "back": {0, 1, 2, 3},
            "belly": {0, 1, 2, 3},
            "underwear": {0, 1},
            "pussy": {0, 1},
            "anus": {0, 1},
        },
    },
    "hides": {
        "standing": {
            "breast": {0, 2},
            "back": {0, 1, 2, 3},
            "belly": {0, 1, 2, 3},
            "pussy": {0, 1},
            "anus": {0, 1},
        },
    },
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Surf's up, [Rogue.Player_petname].")),

        flags = {"change_Clothing", "greenyellow_sleeved_swimsuit"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}