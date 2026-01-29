define Rogue_all_Clothes["black_cami_tanktop"] = {
    "name": _("black cami tanktop"),
    "short_name": _("tanktop"),

    "type": "bra",
    "categories": {
        "tanktop",
        "booby",
        "comfy",

        "singular",
    },

    "shame": (0, 15),
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("This ole' top was the first thing Ah bought out here.")),

        flags = {"change_Clothing", "black_cami_tanktop"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah do like a classic.")),

        flags = {"change_Clothing", "black_cami_tanktop"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}