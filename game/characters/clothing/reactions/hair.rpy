define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah always keep a scrunchie on me.")),

        flags = {"change_Clothing", "before", "hair"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure, lemme just remember where Ah put that scrunchie.")),

        flags = {"change_Clothing", "before", "hair"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure, lemme just grab my brush.")),

        flags = {"change_Clothing", "before", "hair"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Be right back, [Rogue.Player_petname]. Need to find a brush.")),

        flags = {"change_Clothing", "before", "hair"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure thang, lemme just find my brush.")),

        flags = {"change_Clothing", "before", "hair"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure, Ah'll just go muss it up for yah. . .")),

        flags = {"change_Clothing", "before", "hair", "messy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Don't know why Ah even bother to get all dressed up in the mornin'.")),

        flags = {"change_Clothing", "before", "hair", "messy"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Be right back, [Rogue.Player_petname]. Need to find a sink or a pond.")),

        flags = {"change_Clothing", "before", "hair", "wet"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah hope Ah did it right. . .")),

        flags = {"change_Clothing", "after", "hair"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Putting my hair up like this always makes me wanna go for a run, maybe we can find some kinda exercise to do together?")),

        flags = {"change_Clothing", "after", "hair", "breezy"},
        variants = {"ponytail", "updo"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Wet enough for ya [Rogue.Player_petname]?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "hair", "wet"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Never did get fully used to all this hair in my face.")),

        flags = {"change_Clothing", "after", "hair"},
        exclusions = "ponytail",

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Getting my hair to part the first time took ages.")),

        flags = {"change_Clothing", "after", "hair"},
        exclusions = "ponytail",

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Fine, but just 'cause my hair's goin' up doesn't mean Ah'm goin' down on ya. . .")),

        conditions = (
            ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

            ConditionClass("check_approval(Rogue, threshold = 'blowjob')"),
        ),

        flags = {"change_Clothing", "before", "hair"},
        variants = {"ponytail", "updo"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Don't get any ideas about this. . .")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "before", "hair"},
        variants = {"ponytail", "updo"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Sure. . . Ah'll just go muss it up in the sink for yah. . .")),

        flags = {"change_Clothing", "before", "hair", "wet"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Don't get any ideas about me putting my hair up now.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "hair"},
        variants = {"ponytail", "updo"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("You like when Ah look like Ah just rolled out of bed?")),

        secondary = InteractionClass(
            InstructionClass("Rogue.change_mood('flirty')"),

            DialogueClass("ch_Rogue", _(". . . or {i}we{/i} just rolled outta bed together?")),

            conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),
        ),

        flags = {"change_Clothing", "after", "hair", "messy"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah look like you an' me just got done rolling around in the hay.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "hair", "messy"},

        terminal = True,
    ),
}