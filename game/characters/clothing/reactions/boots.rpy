define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure, Ah can try these on. Just gimme a hand gettin' them on, will ya?")),

        flags = {"change_Clothing", "before", "boots"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("These boots are nice 'n sturdy.")),

        flags = {"change_Clothing", "boots"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}