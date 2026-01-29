define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah was startin' to feel a chill - thankfully this thing's got a lining.")),

        flags = {"change_Clothing", "warm", "jacket"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}