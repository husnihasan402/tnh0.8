define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah do like the green. . .")),

        flags = {"gift", "Clothing", "green"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Wow, this is pretty. . .")),

        flags = {"gift", "Clothing"},
        variants = {"fancy", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah like it. . .")),

        flags = {"gift", "Clothing", "singular"},
        variants = {"fancy", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'surprised1', 'surprised2'})"),

        DialogueClass("ch_Rogue", _("[Rogue.Player_petname!c], these are gorgeous. Ah don't think anyone has ever given me anythin' this fancy.")),

        flags = {"gift", "Clothing", "fancy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah'll look good in those.")),

        flags = {"gift", "Clothing", "plural"},
        variants = {"fancy", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Wow, these are sexy.")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_face('flirty', brows = {'worried', None})"),

            DialogueClass("ch_Rogue", _("Not {i}too{/i} sexy, right?")),

            conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),
        ),

        flags = {"gift", "Clothing", "sexy", "plural"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'surprised1', 'surprised2'})"),

        DialogueClass("ch_Rogue", _("Damn, [Player.first_name].")),

        flags = {"gift", "Clothing"},
        variants = {"fancy", "sexy"},

        terminal = False,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah wonder why you like these. . .")),

        flags = {"gift", "Clothing", "sexy", "plural"},

        initial = "optional",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("These look comfy. . .")),

        flags = {"gift", "Clothing", "comfy", "plural"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'confused2', 'confused3'}, eyes = {'side', None})"),

        DialogueClass("ch_Rogue", _("It's gorgeous but. . .")),
        DialogueClass("ch_Rogue", _("I don't know, this is too much.")),

        flags = {"gift", "Clothing", "reject", "fancy", "singular"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'surprised1', 'surprised2'})"),

        DialogueClass("ch_Rogue", _("Oh, thank you!")),

        flags = {"gift", "Clothing"},
        exclusions = "kinky",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah love 'em!")),

        flags = {"gift", "Clothing", "plural"},
        exclusions = "kinky",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("You think Ah could pull this off?")),

        flags = {"gift", "Clothing"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("You think Ah'd look good in somethin' like that?")),

        flags = {"gift", "Clothing", "singular"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("If yer lucky, Ah'll wear it for ya sometime.")),
        
        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"gift", "Clothing", "singular"},
        variants = {"kinky", "sexy"},

        initial = "optional",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Really? Ah guess it is cute. . .")),
        
        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"gift", "Clothing", "singular"},
        variants = {"kinky", "sexy", "bikini"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("It is nice. . .")),
        
        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"gift", "Clothing", "singular"},
        variants = {"kinky", "sexy", "bikini"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah. . . well. . . they are nice. . .")),
        
        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"gift", "Clothing", "plural"},
        variants = {"kinky", "sexy", "bikini"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("For me?")),

        flags = {"gift", "Clothing"},
        variants = {"fancy", "lingerie"},

        terminal = False,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah'd love to dress up for you, [Rogue.Player_petname].")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"gift", "Clothing"},
        variants = {"fancy", "sexy"},

        initial = "optional",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face('flirty', brows = 'raised', eyes = {'down', None})"),

        DialogueClass("ch_Rogue", _("Mah goodness. . .")),
        DialogueClass("ch_Rogue", _("These're beautiful.")),

        flags = {"gift", "Clothing"},
        variants = {"hose", "stockings"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ya better not rip 'em. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"gift", "Clothing"},
        variants = {"hose", "stockings"},
        exclusions = "ripped",

        initial = "optional",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face('flirty', brows = 'raised', eyes = {'down', None})"),

        DialogueClass("ch_Rogue", _("And it looks like ya got my size right.")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_mood('flirty')"),

            DialogueClass("ch_Rogue", _("Thank you, [Rogue.Player_petname].")),
        ),

        flags = {"gift", "Clothing"},
        variants = {"hose", "stockings"},

        initial = False,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'worried1'})"),

        DialogueClass("ch_Rogue", _("Ah can pick out my own clothes, thank you.")),

        flags = {"gift", "Clothing", "reject"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'confused1', 'confused2', 'worried1'})"),

        DialogueClass("ch_Rogue", _("Ah can buy my own clothes, thank you.")),

        flags = {"gift", "Clothing", "reject"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Uhm, no thanks. . .")),

        flags = {"gift", "Clothing", "reject"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("No thank you, [Player.first_name].")),

        flags = {"gift", "Clothing", "reject"},
        exclusions = "kinky",
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Why would Ah even consider it. . . ?")),

        flags = {"gift", "Clothing", "reject", "singular"},
        variants = {"kinky", "sexy"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'angry1', 'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Yeah. . . no. . .")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"kinky", "sexy"},
        exclusions = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Getting ahead of yourself, [Rogue.Player_petname].")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"kinky", "sexy"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'surprised1', 'surprised2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah think it's a bit too soon for gifts like that. . .")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"kinky", "sexy"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah appreciate the offer, but no thanks.")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"sexy", "lingerie"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Uh. . . no thanks, [Rogue.Player_petname].")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"bra", "underwear", "sexy", "lingerie"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah'm all set, thank you very much.")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"bra", "underwear", "sexy", "lingerie"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'confused1', 'confused2', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah don't think that's appropriate. . .")),

        flags = {"gift", "Clothing", "reject"},
        variants = {"bra", "underwear", "kinky", "sexy"},
        optionals = "close_call",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah could wear this for you. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"gift", "Clothing"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("For me? And in my favorite color too?")),

        flags = {"gift", "Clothing", "green"},

        terminal = False,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("These are perfect for date nights!")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("If we go somewhere real fancy that is. . .")),
        ),

        flags = {"gift", "Clothing", "fancy", "plural"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah'll wear 'em whenever ya want.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"gift", "Clothing", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("They look so so sexy, Ah wanna put em on right away for ya.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"gift", "Clothing", "sexy", "plural"},
        exclusions = "kinky",

        terminal = True,
    ),
}