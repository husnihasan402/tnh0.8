define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Better make sure Ah wear something underneath with this one.")),

        secondary = {
            InteractionClass(
                InstructionClass("Rogue.change_mood('flirty')"),

                DialogueClass("ch_Rogue", _("Unless we're in private of course.")),

                conditions = (
                    ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

                    ConditionClass("check_approval(Rogue, threshold = 'see_breasts')"),

                    ConditionClass("not Rogue.check_trait('exhibitionist')"),
                ),
            ),

            InteractionClass(
                InstructionClass("Rogue.change_mood('flirty')"),

                DialogueClass("ch_Rogue", _("Unless ya didn't want me to. . .")),

                conditions = (
                    ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

                    ConditionClass("check_approval(Rogue, threshold = 'see_breasts')"),

                    ConditionClass("Rogue.check_trait('exhibitionist')"),
                ),
            ),
        },

        flags = {"change_Clothing", "top"},
        variants = {"fishnet", "mesh"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Ah feel like ya just wanted an excuse to see me mostly topless.")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'see_breasts')"),

        flags = {"change_Clothing", "after", "top"},
        variants = {"fishnet", "mesh"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood('flirty')"),

        DialogueClass("ch_Rogue", _("Like what you can kinda see?")),

        conditions = ConditionClass("check_approval(Rogue, threshold = 'sexual_flirting')"),

        flags = {"change_Clothing", "after", "top"},
        variants = {"fishnet", "mesh"},

        terminal = True,
    ),
}