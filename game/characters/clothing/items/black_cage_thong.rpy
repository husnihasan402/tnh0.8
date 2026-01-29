define Rogue_all_Clothes["black_cage_thong"] = {
    "name": _("black cage thong"),
    "short_name": _("thong"),

    "type": "underwear",
    "categories": {
        "thong",
        "sexy",
        "lingerie",

        "singular",
    },

    "shop_type": "lingerie",
    "chapter": 1,
    "season": 3,

    "price": 5,

    "shame": (15, 350),
}

define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("It's very. . . strappy.")),

        flags = {"change_Clothing", "black_cage_thong"},
        optionals = {"before", "after"},

        initial = "optional",

        tags = "flavor",
    ),
}