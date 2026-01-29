define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Takin' me swimmin'?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "swimsuit"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah could use a swim, [Rogue.Player_petname].")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "swimsuit"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Takin' me swimmin'? Or just tryna get a better look at my [Rogue.get_body_part_reference('breast')]s?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "swimsuit", "booby"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Like the green, or that they're skimpy?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "bikini", "green", "underwear"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ya like the look?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "swimsuit"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah just love the way this ol' thing makes my body look.")),

        flags = {"change_Clothing", "swimsuit", "singular"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("It's a little nippy, but Ah like the look. . .")),

        flags = {"change_Clothing", "swimsuit", "singular"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("A bit skimpy. . . but Ah like the green.")),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "swimsuit", "green"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("It's a little chilly, but Ah like the look. . .")),

        flags = {"change_Clothing", "bikini"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("A bit skimpy. . . but Ah would swim in 'em. . .")),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "bikini", "plural"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Takin' me swimmin'? Or just tryna get a better look?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "swimsuit"},
        variants = {"booby", "sexy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Truth be told, Ah used to train so hard to control my powers that Ah can get a swimsuit on and off in seconds.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "swimsuit"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ya really thought Ah'd be okay with ya pickin' out bikini bottoms for me. . . ?")),

        flags = {"gift", "Clothing", "bikini", "underwear"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah'm not really comfortable with you pickin' out bikinis for me. . .")),

        flags = {"gift", "Clothing", "reject", "bikini"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Why would you try giftin' me a bikini. . .")),

        flags = {"gift", "Clothing", "reject", "bikini"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Skimpy bikini bottoms. . . really [Rogue.Player_petname]?")),

        flags = {"gift", "Clothing", "reject", "bikini", "underwear"},
        optionals = "close_call",

        terminal = True,
    ),
}