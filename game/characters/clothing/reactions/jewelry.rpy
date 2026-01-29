define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah hope this ain't just Ah kink thing with you. . .")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_face('flirty', eyes = {'side', None}, blush = {0, 1})"),

            DialogueClass("ch_Rogue", _("Unless. . .")),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "collar"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("We should go to a concert sometime, [Rogue.Player_petname].")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Then Ah'll fit right in.")),
        ),

        flags = {"change_Clothing", "spiked"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Do these make me look tough?")),

        flags = {"change_Clothing", "spiked", "plural"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("What is it about the restrained look that does it for you?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "collar"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'smirk1', 'smirk2', 'sympathetic'})"),

        DialogueClass("ch_Rogue", _("Ah've almost gotten used to the weird looks Ah get when this is on.")),

        flags = {"change_Clothing", "collar"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}