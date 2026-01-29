define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Want me to look real heavy metal?")),

        flags = {"change_Clothing", "before", "running_mascara"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Tell ya what, Ah think Ah look sexy in a weird way.")),

        flags = {"change_Clothing", "after", "running_mascara"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Runny enough?")),

        flags = {"change_Clothing", "after", "running_mascara"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2'})"),

        DialogueClass("ch_Rogue", _("You got a lot of nerve asking me t' mess up my makeup.")),

        flags = {"change_Clothing", "reject", "makeup", "messy"},
        exclusions = "close_call",

        terminal = True,
    ),
}