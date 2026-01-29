define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah'm pretty sure Ah own just about one of everythin' in black.")),

        flags = {"change_Clothing", "black"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("A perfect choice with weather like this.")),

        conditions = ConditionClass("temperature[time_index] >= 25"),

        flags = {"change_Clothing", "breezy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Wanna workout?")),

        flags = {"change_Clothing", "athletic"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("We goin' for a workout?")),

        flags = {"change_Clothing", "athletic"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("We goin' for a spar?")),

        flags = {"change_Clothing", "athletic"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("They're real comfy.")),

        flags = {"change_Clothing", "comfy", "plural"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("We goin' out somewhere nice?")),

        flags = {"change_Clothing", "fancy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah love how elegant this thing is.")),

        flags = {"change_Clothing", "fancy", "singular"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah reckon more girls should get decked out in fishnet. . .")),

        flags = {"change_Clothing", "fishnet"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure, Ah can try these on.")),

        flags = {"change_Clothing", "before", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure thang, [Rogue.Player_petname], lemme just slip this on.")),

        flags = {"change_Clothing", "before", "singular"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah just love this thing, it's darin' and comfortable.")),

        flags = {"change_Clothing", "before", "singular"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("This is so cute. . .")),

        flags = {"change_Clothing", "singular"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure, Ah can change into the yellow ones.")),

        flags = {"change_Clothing", "before", "yellow", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ain't this the prettiest thing??")),

        flags = {"change_Clothing", "singular"},
        exclusions = "kinky",
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ain't this just the coolest thang??")),

        flags = {"change_Clothing", "hero", "singular"},
        exclusions = "kinky",
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah love how it fits my style.")),

        flags = {"change_Clothing", "singular"},
        variants = {"black", "spiked"},
        exclusions = "kinky",
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah'd love to hit the town with you later while wearin' this.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "singular"},
        variants = {"fancy", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah hope this doesn't turn too many heads.")),

        flags = "change_Clothing",
        variants = {"kinky", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("A bit skimpy. . . but if it's only you. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = "change_Clothing",
        variants = {"kinky", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ain't these so hot, [Rogue.Player_petname]?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "plural"},
        variants = {"kinky", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Want me to slip these on, huh?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "plural"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah guess you like this one. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = "change_Clothing",
        variants = {"hair", "singular"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ya better not just be tryna see my [Rogue.get_body_part_reference('breast')]s.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "booby"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Tryna get a better look at my [Rogue.get_body_part_reference('breast')]s?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "booby"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Tryin' to catch a glimpse of these legs, [Rogue.Player_petname]?")),
        DialogueClass("ch_Rogue", _("Ah suppose Ah can let ya watch.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "leggy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah know ya like the view when Ah've got these on.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("This one's pretty sexy. . . but if it's only you. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "sexy", "singular"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("We goin' out tonight?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = "change_Clothing",
        variants = {"fancy", "lingerie"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah should wear this next time we go out on a date.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "singular"},
        variants = {"fancy", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah don't mind showin' you a bit of skin.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before"},
        variants = {"bra", "underwear", "sexy", "lingerie"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Tryna get a better look?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before"},
        variants = {"booby", "leggy", "underwear"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Anglin' for a show are we? Ah think Ah can oblige.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before"},
        variants = {"booby", "leggy", "underwear"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Getting all dressed up for you is hot. Better unwrap your presents tonight. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = "change_Clothing",
        variants = {"fancy", "kinky", "lingerie", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ooh, Ah could use a change of color.")),

        flags = {"change_Clothing", "before"},
        exclusions = {"black", "green", "yellow"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sometimes Ah put these on just to lounge around my room, they're so comfortable.")),

        flags = {"change_Clothing", "comfy", "plural"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Lemme just shimmy these on. . .")),

        flags = {"change_Clothing", "before", "tight"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("This doesn't leave much to the imagination. . .")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("But Ah love the look on yer face right now.")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        flags = {"change_Clothing", "singular"},
        variants = {"kinky", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("So comfy!")),

        flags = {"change_Clothing", "comfy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("These are some of my favorites.")),

        flags = {"change_Clothing", "plural"},
        exclusions = "kinky",
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah guess if you want.")),

        flags = {"change_Clothing", "before"},
        variants = {"kinky", "towel"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("We goin' for a run?")),

        flags = "change_Clothing",
        variants = {"footwear", "tights"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("You wanna see me in just a towel? Ah suppose Ah can oblige.")),

        flags = {"change_Clothing", "before", "towel"},

        terminal = True,
    ),
}