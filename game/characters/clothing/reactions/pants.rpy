define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Are they {i}too{/i} short?")),

        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "after", "shorts"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("They're a bit snug in the back. . .")),

        flags = {"change_Clothing", "after", "pants", "tight"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("We workin' out, or did ya just want a good look at my [Rogue.get_body_part_reference('ass')]?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "shorts", "athletic"},
        variants = {("shorts", "athletic"), ("tights", "athletic")},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Do these jeans make my [Rogue.get_body_part_reference('ass')] look okay?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "jeans"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Some comfy shorts? Good call.")),

        flags = {"gift", "Clothing", "shorts", "comfy"},

        terminal = True,
    ),
}