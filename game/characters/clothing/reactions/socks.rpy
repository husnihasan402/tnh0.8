define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Better not just be a foot thing. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "socks"},
        optionals = {"before", "after"},

        terminal = True,
    ),
    
    InteractionClass(
        DialogueClass("ch_Rogue", _("Before Ah came here Ah don't think Ah owned any socks that started below the knee.")),

        flags = {"change_Clothing", "ankle_socks"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("These socks are perfect to pair with my runnin' shoes.")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Ah'm just glad Ah finally have someone to run with.")),

            conditions = ConditionClass("EventScheduler.check('Rogue_events_chapter_one_season_one_jogging')"),
        ),

        flags = {"change_Clothing", "ankle_socks"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Like wearin' nothin' at all!")),

        flags = {"change_Clothing", "ankle_socks"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Now you can barely tell Ah'm wearin' socks.")),

        flags = {"change_Clothing", "after", "ankle_socks"},

        terminal = True,
    ),
}