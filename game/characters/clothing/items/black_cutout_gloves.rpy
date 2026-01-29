define Rogue_all_Clothes["black_cutout_gloves"] = {
    "name": _("black cutout gloves"),
    "short_name": _("gloves"),

    "type": "gloves",
    "categories": {
        "functional",
        "accessory",

        "plural",
    },
}

define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Funnily enough, Ah had these before my powers came in. . .")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("This whole goth thing really came in handy.")),
        ),

        flags = {"change_Clothing", "black_cutout_gloves"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}