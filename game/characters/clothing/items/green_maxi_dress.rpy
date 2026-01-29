define Rogue_all_Clothes["green_maxi_dress"] = {
    "name": _("green maxi dress"),
    "short_name": _("dress"),

    "type": "dress",
    "categories": {
        "fancy",
        "booby",

        "singular",
    },

    "chapter": 1,
    "season": 4,
    
    "price": 10,

    "covers": {
        "standing": {
            "bra": {0},
            "breast": {0},
            "back": {0, 1},
            "belly": {0, 1},
            "thigh": {0, 1},
            "underwear": {0, 1},
            "ass": {0, 1},
            "pussy": {0, 1},
            "anus": {0, 1},
        },
    },
    "hides": {
        "standing": {
            "breast": {0},
            "back": {0, 1},
            "belly": {0, 1},
            "thigh": {0, 1},
            "underwear": {0, 1},
            "ass": {0, 1},
            "pussy": {0, 1},
            "anus": {0, 1},
        },
    },

    "traits": {
        "supports_breasts": {0},
    },
}

define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_face({'surprised2', 'surprised3'})"),

        DialogueClass("ch_Rogue", _("My lord!")),
        DialogueClass("ch_Rogue", _("This looks like somethin' that belongs on the red carpet. Ah can't wait to wear it out and about!")),

        flags = {"gift", "Clothing", "green_maxi_dress"},

        tags = {"accept", "flavor"},
    ),
}