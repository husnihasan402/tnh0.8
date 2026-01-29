define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Why don't we go get dinner or somethin', this is the perfect dress for a night out.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "dress", "fancy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Learnin' how to walk in this thing took. . . some time.")),

        flags = {"change_Clothing", "dress", "fancy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("If Ah hike it up, we could still. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "dress", "fancy"},

        terminal = True,
    ),
}