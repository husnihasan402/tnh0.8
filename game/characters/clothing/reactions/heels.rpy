define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ya sure you wanna give up your height advantage out here, [Rogue.Player_petname]?")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Ah mean. . . Ah'm still a couple inches short, but. . .")),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "heels"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah'm going to strut my stuff out here.")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_mood('flirty')"),

            DialogueClass("ch_Rogue", _("And you better stare.")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        flags = {"change_Clothing", "heels"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face('sympathetic')"),

        DialogueClass("ch_Rogue", _("Still ain't taller than you with these on.")),

        flags = {"change_Clothing", "after", "heels"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Real cute, right?")),

        flags = {"change_Clothing", "after", "footwear"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("You takin' me out somewhere fancy, or just got a thing for heels?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "heels", "fancy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1'})"),

        DialogueClass("ch_Rogue", _("If yer gonna take me out, we better go now - these are hell on my feet.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "after", "heels"},

        terminal = True,
    ),
    
    InteractionClass(
        InstructionClass("Rogue.change_face({'angry3', 'appalled1', 'appalled2'})"),

        DialogueClass("ch_Rogue", _("Buyin' me stripper heels?")),
        DialogueClass("ch_Rogue", _("You must've lost yer damn mind.")),

        flags = {"gift", "Clothing", "reject", "stilettos"},
        exclusions = "close_call",

        terminal = True,
    ),
}