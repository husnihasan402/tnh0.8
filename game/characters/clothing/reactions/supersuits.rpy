define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah love the colors.")),

        flags = {"change_Clothing", "supersuit"},
        optionals = {"before", "after", "hero"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ya wanna see me in my ol' combat getup?")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Gonna get some trainin' in?")),
        ),

        flags = {"change_Clothing", "before", "supersuit"},
        optionals = "hero",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("A bit form fittin'. . .")),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "after", "supersuit"},
        optionals = "hero",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah designed 'er myself. Originally we all had some yellow on our costumes.")),
        
        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Ah hated it to start, but it's grown on me.")),
        ),
        
        flags = {"change_Clothing", "supersuit"},
        optionals = {"before", "after", "hero"},

        terminal = True,
    ),
}