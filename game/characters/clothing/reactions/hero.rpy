define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Cool, right?")),

        flags = {"change_Clothing", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Pretty sure Ah could fit half of what I own in one of these.")),

        flags = {"change_Clothing", "belt"},
        variants = {"functional", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sometimes Ah keep fruit snacks in here for between Danger Room sessions - apple's my favorite.")),

        flags = {"change_Clothing", "belt"},
        variants = {"functional", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Think Ah should wear this to a movie, [Rogue.Player_petname]? Ah'm pretty sure Ah could fit a full course meal in here.")),

        flags = {"change_Clothing", "belt"},
        variants = {"functional", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Now where did Ah put my room key.")),

        flags = {"change_Clothing", "after", "belt"},
        variants = {"functional", "hero"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Heh, it's nice to actually have a place to hold stuff.")),

        flags = {"change_Clothing", "belt"},
        variants = {"functional", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("To be honest, [Rogue.Player_petname], Ah think it could use more pouches.")),

        flags = {"change_Clothing", "belt"},
        variants = {"functional", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Truth be told, she's much better than a purse.")),

        flags = {"change_Clothing", "belt"},
        variants = {"functional", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}