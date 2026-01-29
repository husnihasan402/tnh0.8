define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah love this bra. . .")),

        flags = {"change_Clothing", "bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah really dig that bra.")),

        flags = {"change_Clothing", "bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah do like the support. . .")),

        flags = {"change_Clothing", "sports_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Funny enough, Ah think this is the only piece of my getup Ah've never broken.")),

        flags = {"change_Clothing", "sports_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face('sympathetic')"),

        DialogueClass("ch_Rogue", _("This thing can get so sweaty.")),

        flags = {"change_Clothing", "sports_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("You wouldn't believe the support this bra has. . .")),

        flags = {"change_Clothing", "sports_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("This thing has singlehandedly saved my back.")),

        flags = {"change_Clothing", "sports_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah could just go topless for ya, but this bra is nice too. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'see_breasts')"),

        flags = {"change_Clothing", "bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah ever tell you that Ah can get one of these off with one hand?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah can barely comprehend how this thing holds my [Rogue.get_body_part_reference('breast')]s back.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "sports_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ain't this thing so sleek?")),

        flags = {"change_Clothing"},
        variants = {"black_cage_bra", "black_keyhole_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah think Ah'd wear this out if Ah was dressin' up as some kinda vampire queen of the dead.")),

        flags = {"change_Clothing"},
        variants = {"black_cage_bra", "black_keyhole_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah just love getting all vamped up for you!")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing"},
        variants = {"black_cage_bra", "black_keyhole_bra"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'confused1', 'confused2', 'surprised1', 'surprised2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah'd rather you not buy me bras. . .")),

        flags = {"gift", "Clothing", "reject", "bra"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'surprised1', 'surprised2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah'm not interested in your bra preferences.")),

        flags = {"gift", "Clothing", "reject", "bra"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'confused1', 'confused2', 'surprised1', 'surprised2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah'm not really comfortable with you pickin' out bras for me.")),

        flags = {"gift", "Clothing", "reject", "bra"},
        exclusions = "close_call",

        terminal = True,
    ),
}