# TODO: revise
define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("What do ya think, [Rogue.Player_petname]?")),

        flags = {"change_Clothing", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Like this?")),

        flags = {"change_Clothing", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("How's that?")),

        flags = {"change_Clothing", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Comfy.")),

        flags = {"change_Clothing", "after", "comfy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Iconic.")),

        flags = {"change_Clothing", "after", "hero"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ain't fishnet just the coolest thang??")),

        flags = {"change_Clothing", "after", "fishnet"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Now Ah look like somethin' right out of one of my favorite music videos.")),

        flags = {"change_Clothing", "after", "fishnet"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Doesn't lace look amazin' on me?")),

        flags = {"change_Clothing", "after", "lace"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah just love the way this fabric feels, it's like a cloud.")),

        flags = {"change_Clothing", "after", "mesh"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah like 'em.")),

        flags = {"change_Clothing", "after", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah really dig 'em.")),

        flags = {"change_Clothing", "after", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah do look good in 'em.")),

        flags = {"change_Clothing", "after", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Don't mind wearin' these for you.")),

        flags = {"change_Clothing", "after", "sexy", "plural"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("This ol' thing's really flatterin', don't you think?")),

        flags = {"change_Clothing", "after", "singular"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Doesn't this thang make my [Rogue.get_body_part_reference('breast')]s look incredible?")),

        flags = {"change_Clothing", "after", "booby", "singular"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Doesn't this thing make my waist look incredible?")),

        flags = {"change_Clothing", "after", "fancy", "singular"},
        variants = {"dress", "skirt"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah don't think Ah ever had somethin' real frilly back home.")),

        flags = {"change_Clothing", "after", "lace", "singular"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah'd love to hit the town tonight in these [Rogue.Player_petname].")),

        flags = {"change_Clothing", "after", "footwear", "fancy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("[Rogue.Player_petname!c], ya'know Ah look great in yellow. . .")),

        flags = {"change_Clothing", "after", "yellow"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah like the way these feel on my skin.")),

        flags = {"change_Clothing", "after", "comfy", "plural"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Don't these make my [Rogue.get_body_part_reference('ass')] look great?")),

        flags = {"change_Clothing", "after", "plural"},
        variants = {"pants", "tights", "underwear"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Real stylish.")),

        flags = {"change_Clothing", "after"},
        exclusions = "kinky",

        terminal = True,
    ),

    InteractionClass(
        flags = {"change_Clothing", "after", "singular"},
        exclusions = "kinky",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah always love wearin' these.")),

        flags = {"change_Clothing", "after", "plural"},
        exclusions = "kinky",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Plain but comfy.")),

        flags = {"change_Clothing", "after", "comfy"},
        exclusions = {"fancy", "kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah do love how it looks on me.")),

        flags = {"change_Clothing", "after"},
        variants = {"hair", "singular"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah hope the wind dies down, this thing is breezy.")),

        flags = {"change_Clothing", "after", "breezy", "singular"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah look like someone's secretary.")),

        flags = {"change_Clothing", "after"},
        variants = {"hose", "stockings"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah swear, if Ah get a run in these, somebody's gettin' hurt.")),

        flags = {"change_Clothing", "after"},
        variants = {"hose", "stockings"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("So. . . what do ya think?")),

        flags = {"change_Clothing", "after"},
        variants = {"fancy", "kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah feel like this one will never go out of style?")),

        flags = {"change_Clothing", "after"},
        variants = {"hair", "singular"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah feel really sexy.")),

        flags = {"change_Clothing", "after"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("[Rogue.Player_petname!c], Ah'm certain to turn heads in this getup.")),

        flags = {"change_Clothing", "after"},
        variants = {"kinky", "towel"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah think these make me look real sexy, don't you?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "plural"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah put 'em on, just like ya wanted.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "plural"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("This sure does distract you, huh?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "singular"},
        variants = {"kinky", "lingerie", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Just say the word if ya want a peek underneath.")),

        conditions = (
            ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

            ConditionClass("check_approval(Rogue, threshold = 'see_pussy')"),
        ),

        flags = {"change_Clothing", "after"},
        variants = {"bra", "underwear", "sexy", "lingerie"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Enjoyin' the view?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "plural"},
        variants = {"pants", "skirt", "tights", "underwear"},

        terminal = True,
    ),
    InteractionClass(
        DialogueClass("ch_Rogue", _("There we go, [Rogue.Player_petname].")),

        flags = {"change_Clothing", "after"},

        terminal = True,
    ),


    InteractionClass(
        DialogueClass("ch_Rogue", _("Aren't they flattering?")),

        flags = {"change_Clothing", "after", "plural"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah can tell yer starin' at my [Rogue.get_body_part_reference('ass')]. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after"},
        variants = {"pants", "tights", "underwear"},

        initial = "optional",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Want me to do a spin for ya?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after"},
        variants = {"dress", "skirt"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah love gettin' all dolled up for ya. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after"},
        variants = {"fancy", "lingerie"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah bet Ah look like yer private dancer. . .")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Ah could be. . .")),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after"},
        variants = {"hose", "stockings"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("You should take me somewhere fancy, Ah don't wanna get dressed up for nothin'.")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("That is, unless ya had {i}other{/i} plans for me tonight. . .")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "after"},
        variants = {"fancy", "lingerie"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Like what ya see? Cause Ah certainly like yer starin'.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah feel real sexy in this getup. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("[Rogue.Player_petname!c], it's a little breezy but. . .")),
        DialogueClass("ch_Rogue", _("Ah feel real sexy in this getup.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "sexy", "breezy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Don't get too worked up now, [Rogue.Player_petname].")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Who am Ah kiddin', Ah turn myself on in these.")),
        ),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "sexy", "plural"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah wonder why you like these so much. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "plural"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Maybe sometime we can race?")),

        flags = {"change_Clothing", "after"},
        variants = {("sneakers", "athletic"), "swimsuit"},

        initial = "optional",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Maybe we can do some one-on-one exercisin' later.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "athletic"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Yer gonna have to take me out somewhere nice so Ah can strut my stuff in these.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "after", "footwear", "fancy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah'd love to hit the town with ya tonight in these, [Rogue.Player_petname].")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'dating')"),

        flags = {"change_Clothing", "after", "footwear", "fancy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah hope nobody sees. . .")),

        secondary = InteractionClass(
            DialogueClass("ch_Rogue", _("Except for you of course.")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "after"},
        variants = {"kinky", "sexy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Gettin' all dressed up for you makes me want t' run back to the dorms with you, [Rogue.Player_petname]. . .")),

        conditions = (
            ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

            ConditionClass("Player.location not in Bedrooms"),
        ),

        flags = {"change_Clothing", "after"},
        variants = {"kinky", "sexy", "fancy"},

        terminal = True,
    ),
}