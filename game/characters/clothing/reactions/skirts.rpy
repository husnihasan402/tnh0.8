define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("It ain't the most modest skirt, but it ain't too skimpy neither. . .")),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "skirt"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("This thing makes my [Rogue.get_body_part_reference('ass')] look incredible, don't it?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "skirt"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face('flirty', eyes = {'down', None})"),

        DialogueClass("ch_Rogue", _("This thing rides up something fierce when Ah sit down. . .")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_mood('flirty')"),
            
            DialogueClass("ch_Rogue", _("Want a peek?")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'see_underwear')"),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "skirt"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}