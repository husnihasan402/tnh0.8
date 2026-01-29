define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah've started wearin' these out on missions. Nothing worse than a wedgie in a skintight costume.")),

        flags = {"change_Clothing", "boyshorts", "comfy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("[JeanGrey.public_name] told me how comfortable these things are - she wasn't kiddin'.")),

        conditions = ConditionClass("Rogue.get_friendship(JeanGrey) >= 1"),

        flags = {"change_Clothing", "boyshorts"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("My last pair were getting a little wet. . .")),

        conditions = (
            ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

            ConditionClass("Rogue.desire >= 0.5"),
        ),

        flags = {"change_Clothing", "after", "underwear"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Maybe you can take these off of me sometime, [Rogue.Player_petname].")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'see_pussy')"),

        flags = {"change_Clothing", "underwear"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Happy to oblige, [Rogue.Player_petname]. . .")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_mood('flirty')"),

            DialogueClass("ch_Rogue", _("Ah was gettin' a bit too wet anyway.")),

            conditions = (
                ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

                ConditionClass("Rogue.desire >= 0.5"),
            ),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "underwear"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Maybe Ah should just ask ya which panties to wear every mornin'. It would save me a hell of a lot of time.")),

        conditions = ConditionClass("Rogue in Partners"),

        flags = {"change_Clothing", "panties"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'surprised1', 'surprised2'})"),

        PauseClass(1.0),

        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah've never had lacy panties before.")),

        flags = {"gift", "Clothing", "lace", "panties"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah appreciate the thought, but we're not at the buyin' panties stage, [Rogue.Player_petname].")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"gift", "Clothing", "reject", "panties"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah can pick out my own underwear, thanks.")),

        flags = {"gift", "Clothing", "reject", "underwear"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'appalled1', 'appalled2', 'confused1', 'confused2'})"),

        DialogueClass("ch_Rogue", _("Don't you go thinkin' about what underwear Ah do or don't need.")),

        flags = {"gift", "Clothing", "reject", "underwear"},
        exclusions = "close_call",

        terminal = True,
    ),
}