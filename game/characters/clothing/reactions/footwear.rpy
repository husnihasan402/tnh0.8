define Rogue_interactions |= {
    InteractionClass(
        DialogueClass("ch_Rogue", _("Ah'd love to go on a hike sometime.")),

        flags = {"change_Clothing", "footwear", "athletic"},
        optionals = {"before", "after"},

        terminal = True,
    ),
    
    InteractionClass(
        DialogueClass("ch_Rogue", _("These are so much more comfortable than my boots.")),

        flags = {"change_Clothing", "footwear", "comfy"},
        optionals = {"before", "after"},

        terminal = True,
    ),

    InteractionClass(
        DialogueClass("ch_Rogue", _("Prof. X should up our salary just so Ah don't go broke buyin' new runnin' shoes every few months.")),

        flags = {"change_Clothing", "sneakers", "athletic"},
        optionals = {"before", "after"},

        terminal = True,
    ),
}