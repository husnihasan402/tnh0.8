init python:

    def Rogue_default_Outfits():
        Outfits = []
        
        # Casual 1
        Outfits.append(OutfitClass(Rogue, "Повседневка 1", flags = ("public", "fall", "spring")))

        bra = ClothingClass(Rogue, "black_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_panties")
        underwear.give_trait("default")

        Outfits[-1].Clothes.update({
            "bra": bra, "underwear": underwear,
            "pants": ClothingClass(Rogue, "black_jeans"), "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "top": ClothingClass(Rogue, "black_lowcut_top"),
            "gloves": ClothingClass(Rogue, "black_gloves")})

        # Casual 2
        Outfits.append(OutfitClass(Rogue, "Повседневка 2", flags = ("public", "fall", "spring", "summer")))

        bra = ClothingClass(Rogue, "black_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_panties")
        underwear.give_trait("default")

        hose = ClothingClass(Rogue, "black_tights")
        hose.give_trait("seasonal", value = ["fall", "spring"])

        top = ClothingClass(Rogue, "black_fishnet_top")
        top.give_trait("seasonal", value = ["fall", "spring"])

        Outfits[-1].Clothes.update({
            "bra": bra, "underwear": underwear, "hose": hose,
            "pants": ClothingClass(Rogue, "dark_denim_shorts"), "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "top": top,
            "neck": ClothingClass(Rogue, "black_spiked_collar"), "gloves": ClothingClass(Rogue, "black_gloves"), "sleeves": ClothingClass(Rogue, "black_spiked_bracelets"),
            "jacket": ClothingClass(Rogue, "black_NIN_shirt")})

        # Casual 3
        Outfits.append(OutfitClass(Rogue, "Повседневка 3", flags = ("public", "fall", "winter")))

        bra = ClothingClass(Rogue, "black_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_panties")
        underwear.give_trait("default")

        jacket = ClothingClass(Rogue, "greybrown_plaid_jacket")
        jacket.give_trait("outdoors")

        Outfits[-1].Clothes.update({
            "bra": bra, "underwear": underwear, "hose": ClothingClass(Rogue, "black_tights"),
            "footwear": ClothingClass(Rogue, "black_thighhigh_boots"),
            "dress": ClothingClass(Rogue, "green_sweater_dress"),
            "gloves": ClothingClass(Rogue, "black_gloves"),
            "jacket": jacket})

        # Exercise
        Outfits.append(OutfitClass(Rogue, "Тренировочный", flags = ("exercise", "fall", "winter", "spring", "summer")))

        hose = ClothingClass(Rogue, "green_running_tights")

        if "green_athletic_shorts" in Rogue.Wardrobe.Clothes:
            hose.give_trait("seasonal", value = ["fall", "winter", "spring"])
            hose.give_trait("seasonal_replaced_by", value = ["green_athletic_shorts"])

        Outfits[-1].Clothes.update({
            "hair": ClothingClass(Rogue, "messy_ponytail"),
            "bra": ClothingClass(Rogue, "black_sports_bra"), "underwear": ClothingClass(Rogue, "yellow_panties"), "hose": hose, "socks": ClothingClass(Rogue, "black_ankle_socks"), 
            "footwear": ClothingClass(Rogue, "blackgreen_sneakers"),
            "gloves": ClothingClass(Rogue, "black_gloves")})

        # Hero (Chapter I)
        Outfits.append(OutfitClass(Rogue, "Геройский (Часть I)", flags = ("hero", "fall", "winter", "spring", "summer")))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": ClothingClass(Rogue, "green_headband"),
            "bra": ClothingClass(Rogue, "black_sports_bra"), "underwear": ClothingClass(Rogue, "yellow_panties"),
            "bodysuit": ClothingClass(Rogue, "greenyellow_classic_suit"),
            "footwear": ClothingClass(Rogue, "yellow_classic_boots"),
            "gloves": ClothingClass(Rogue, "yellow_gloves"), "belt": ClothingClass(Rogue, "brown_utility_belt"),
            "jacket": ClothingClass(Rogue, "brown_classic_jacket")})

        # Swimsuit (One-Piece)
        Outfits.append(OutfitClass(Rogue, "Купальник (Цельный)", flags = ("swim", "fall", "winter", "spring", "summer")))

        Outfits[-1].Clothes.update({
            "bodysuit": ClothingClass(Rogue, "greenyellow_sleeved_swimsuit")})

        Outfits[-1].give_trait("no_bra")
        Outfits[-1].give_trait("no_underwear")

        # Swimsuit (Bikini)
        Clothes = {
            "bra": ClothingClass(Rogue, "green_bikini_top"), "underwear": ClothingClass(Rogue, "green_bikini_bottoms")}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass(Rogue, "Купальник (Бикини)", flags = ("swim", "fall", "winter", "spring", "summer")))

            Outfits[-1].Clothes.update(Clothes)

        # Datenight 1
        Outfits.append(OutfitClass(Rogue, "Свидание 1", flags = ("public", "date", "fall", "spring", "summer")))

        bra = ClothingClass(Rogue, "black_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_panties")
        underwear.give_trait("default")

        Outfits[-1].Clothes.update({
            "bra": bra, "underwear": underwear, "hose": ClothingClass(Rogue, "black_tights"), 
            "skirt": ClothingClass(Rogue, "black_leather_skirt"), "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "top": ClothingClass(Rogue, "green_mesh_top"),
            "neck": ClothingClass(Rogue, "black_spiked_collar"), "gloves": ClothingClass(Rogue, "black_gloves")})
        
        # Datenight 2
        Outfits.append(OutfitClass(Rogue, "Свидание 2", flags = ("public", "date", "fall", "spring", "summer")))

        underwear = ClothingClass(Rogue, "yellow_panties")
        underwear.give_trait("default")

        hose = ClothingClass(Rogue, "black_tights")
        hose.give_trait("outdoors")
        hose.give_trait("seasonal", value = ["fall"])

        neck = ClothingClass(Rogue, "black_spiked_collar")
        neck.give_trait("optional")

        sleeves = ClothingClass(Rogue, "black_spiked_bracelets")
        sleeves.give_trait("optional")

        jacket = ClothingClass(Rogue, "brown_classic_jacket")
        jacket.give_trait("outdoors")
        jacket.give_trait("seasonal", value = ["fall"])

        Outfits[-1].Clothes.update({
            "underwear": underwear, "hose": hose,
            "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "dress": ClothingClass(Rogue, "yellow_summer_dress"),
            "neck": neck, "gloves": ClothingClass(Rogue, "black_gloves"), "sleeves": sleeves,
            "jacket": jacket})

        # Formal
        Clothes = {
            "underwear": ClothingClass(Rogue, "yellow_panties"),
            "footwear": ClothingClass(Rogue, "black_heels"),
            "dress": ClothingClass(Rogue, "green_maxi_dress"),
            "gloves": ClothingClass(Rogue, "black_gloves")}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass(Rogue, "Официальный"))

            Outfits[-1].Clothes.update(Clothes)

        # Pajamas
        Outfits.append(OutfitClass(Rogue, "Пижама", flags = ("sleep", "fall", "winter", "spring", "summer")))

        underwear = ClothingClass(Rogue, "yellow_panties")
        underwear.give_trait("default")

        Outfits[-1].Clothes.update({
            "bra": ClothingClass(Rogue, "black_tanktop"), "underwear": underwear})

        # Lingerie 1
        Clothes = {
            "bra": ClothingClass(Rogue, "green_lace_bra"), "underwear": ClothingClass(Rogue, "green_lace_panties"), "hose": ClothingClass(Rogue, "black_garterbelt"), "socks": ClothingClass(Rogue, "black_stockings")}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass(Rogue, "Белье 1", flags = ("sexy",)))

            Outfits[-1].Clothes.update(Clothes)

        # Lingerie 2
        Clothes = {
            "underwear": ClothingClass(Rogue, "green_thong"),
            "dress": ClothingClass(Rogue, "green_lace_nighty")}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass(Rogue, "Белье 2", flags = ("sexy",)))

            Outfits[-1].Clothes.update(Clothes)

        # Nude
        Outfits.append(OutfitClass(Rogue, "Голышом"))

        Outfits[-1].Clothes.update({})
                
        return Outfits