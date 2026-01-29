define Rogue_all_Clothes["green_mesh_top"] = {
    "name": _("green mesh top"),
    "short_name": _("top"),

    "type": "top",
    "categories": {
        "booby",
        "mesh",
        "sexy",

        "singular",
    },

    "chapter": 1,
    "season": 4,

    "covers": {
        "standing": {
            "bra": {0},
            "breast": {0},
            "back": {0},
            "belly": {0},
        },
    },
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("You like the retro look, [Rogue.Player_petname]?")),

        flags = {"change_Clothing", "green_mesh_top"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}