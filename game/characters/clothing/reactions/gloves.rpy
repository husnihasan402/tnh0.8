define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah felt weird not havin' 'em on already.")),

        flags = {"change_Clothing", "before", "gloves"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("They're not my usual casual gloves, but Ah don't mind wearin' em around.")),

        flags = {"change_Clothing", "gloves", "hero"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Sometimes Ah wish Ah didn't need 'em.")),

        flags = {"change_Clothing", "gloves"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("You'd be surprised at how many different ways you can style gloves.")),

        flags = {"change_Clothing", "gloves"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah'm so used to wearin' gloves, Ah forget Ah have any on sometimes.")),

        flags = {"change_Clothing", "gloves"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah just love the way yellow looks on my skin, don't you?")),

        flags = {"change_Clothing", "after", "gloves", "yellow"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah guess this power of mine has some benefits.")),

        flags = {"change_Clothing", "gloves"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Always feel better with a good pair of gloves on. . .")),

        flags = {"change_Clothing", "gloves"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}