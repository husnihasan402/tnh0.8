define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("This ole thing's a lifesaver out in the field.")),

        flags = {"change_Clothing", "headband"},
        optionals = {"before", "after", "hero"},

        terminal = True,
    ),

    InteractionClass(
        InstructionClass("Rogue.change_face('sympathetic')"),

        DialogueClass("ch_Rogue", _("One time Ah was sparrin' and Ah forgot to put my hair up, accidentally gave someone a black eye 'cause Ah couldn't see.")),

        flags = {"change_Clothing", "headband"},
        optionals = {"before", "after", "hero"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Can't tell you how much Ah used to get hair in my face during Danger Room sessions before Ah bought one of these.")),

        flags = {"change_Clothing", "headband"},
        optionals = {"before", "after", "hero"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Don't Ah look like Ah belong on the cover of an old workout VHS tape?")),

        flags = {"change_Clothing", "after", "headband"},
        optionals = "hero",

        terminal = True,
    ),
}