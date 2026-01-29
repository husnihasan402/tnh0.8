define Rogue_interactions |= {
    InteractionClass(
        InstructionClass("Rogue.change_face({'anxious', 'sympathetic', 'worried1', 'worried2'})"),

        DialogueClass("ch_Rogue", _("Ah know people are gonna stare, but Ah swear this looks bad on purpose.")),
        
        conditions = ConditionClass("not Rogue.check_trait('exhibitionist')"),

        flags = {"change_Clothing", "after", "messy"},

        terminal = True,
    ),
}