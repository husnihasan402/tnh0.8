define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_face('confused1')"),

        DialogueClass("ch_Rogue", _("Ah'm good like this.")),

        flags = {"change_Clothing", "reject"},
        optionals = "close_call",

        terminal = True,
    ),
}