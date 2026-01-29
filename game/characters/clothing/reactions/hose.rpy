define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah'd love to wear these to that steakhouse sometime.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "pantyhose"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Tights under a skirt is a great way to keep my modesty. . .")),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "tights"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah hope Ah don't get a run in these anytime soon.")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_mood('flirty')"),

            DialogueClass("ch_Rogue", _("You better be mindful of those hands.")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        flags = {"change_Clothing", "hose"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Does the old fashioned look turn you on?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "pantyhose"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Just to let you know, these go all the way up.")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_face('sly')"),

            DialogueClass("ch_Rogue", _("Ah could give a peek if ya wanted. . .")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'see_underwear')"),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "pantyhose"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}