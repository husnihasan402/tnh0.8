define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_face('flirty', brows = {'cocked', None})"),

        DialogueClass("ch_Rogue", _("What is it that makes these things so attractive?")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_face('flirty', brows = {'cocked', None})"),

            DialogueClass("ch_Rogue", _("Is it the way they frame my stomach? Is it a foot thing?")),

            secondary = InteractionClass(
                InstructionClass("Rogue.change_mood('flirty')"),

                DialogueClass("ch_Rogue", _("Ah can't tell.")),
            ),
        ),

        flags = {"change_Clothing", "garterbelt"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah don't think Ah'll ever get enough lingerie.")),

        flags = {"change_Clothing", "lingerie"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Wasn't easy to learn how to put this thing on for the first time.")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("But it's worth it for the look on yer face.")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        flags = {"change_Clothing", "garterbelt"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Best thing about livin' out here. . . all the options for lingerie.")),

        flags = {"change_Clothing", "lingerie"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Puttin' these on makes me feel hot. . .")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Maybe Ah'll let ya take 'em off me later.")),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "lingerie", "plural"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah just love the idea of goin' out tonight in somethin' real fancy.")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Think you'd be able to control yerself knowin' what Ah got on underneath?")),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "garterbelt"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Lord, all the lingerie Ah want t' show off for you. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "lingerie"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'angry2', 'appalled1', 'appalled2'})"),

        DialogueClass("ch_Rogue", _("This your way of askin' me to be your mistress or somethin'?")),

        conditions = (
            ConditionClass("Partners"),

            ConditionClass("Rogue not in Partners"),
        ),

        flags = {"gift", "Clothing", "reject", "lingerie"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2'})"),

        DialogueClass("ch_Rogue", _("Sorry, [Rogue.Player_petname], Ah don't take lingerie from no one.")),

        conditions = ConditionClass("not check_approval(Rogue, threshold = 'relationship')"),

        flags = {"gift", "Clothing", "reject", "lingerie"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'angry2', 'appalled1', 'appalled2'})"),

        DialogueClass("ch_Rogue", _("Ah don't want you buyin' lingerie for me, 'specially not somethin' this expensive.")),

        conditions = ConditionClass("not check_approval(Rogue, threshold = 'relationship')"),

        flags = {"gift", "Clothing", "reject", "lingerie"},
        exclusions = "close_call",

        terminal = True,
    ),
}