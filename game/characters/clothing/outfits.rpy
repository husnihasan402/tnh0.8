init python:

    def Rogue_default_Outfits() -> list[OutfitClass]:
        Outfits = []
        
        # Casual 1
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Casual 1", 
                flags = {"public", "fall", "spring"},
            ),
        )

        bra = ClothingClass(Rogue, "black_cami_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_cotton_panties")
        underwear.give_trait("default")

        Outfits[-1].Clothes.update({
            "bra": bra, 
            "underwear": underwear,
            "pants": ClothingClass(Rogue, "black_tight_jeans"), 
            "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "top": ClothingClass(Rogue, "black_lowcut_top"),
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"),
        })

        # Casual 2
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Casual 2", 
                flags = {"public", "fall", "spring", "summer"},
            ),
        )

        bra = ClothingClass(Rogue, "black_cami_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_cotton_panties")
        underwear.give_trait("default")

        hose = ClothingClass(Rogue, "black_sheer_pantyhose")
        hose.give_trait("seasonal", value = {"fall", "spring"})

        top = ClothingClass(Rogue, "black_fishnet_top")
        top.give_trait("seasonal", value = {"fall", "spring"})

        Outfits[-1].Clothes.update({
            "bra": bra, 
            "underwear": underwear, 
            "hose": hose,
            "pants": ClothingClass(Rogue, "dark_denim_shorts"), 
            "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "top": top,
            "neck": ClothingClass(Rogue, "black_spiked_collar"), 
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"), 
            "sleeves": ClothingClass(Rogue, "black_spiked_bracelets"),
            "jacket": ClothingClass(Rogue, "black_NIN_shirt"),
        })

        # Casual 3
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Casual 3", 
                flags = {"public", "fall", "winter"},
            ),
        )

        bra = ClothingClass(Rogue, "black_cami_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_cotton_panties")
        underwear.give_trait("default")

        jacket = ClothingClass(Rogue, "greybrown_plaid_jacket")
        jacket.give_trait("outdoors")

        Outfits[-1].Clothes.update({
            "bra": bra, 
            "underwear": underwear, 
            "hose": ClothingClass(Rogue, "black_sheer_pantyhose"),
            "footwear": ClothingClass(Rogue, "black_thighhigh_boots"),
            "dress": ClothingClass(Rogue, "green_sweater_dress"),
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"),
            "jacket": jacket,
        })

        # Exercise
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Exercise", 
                flags = {"exercise", "fall", "winter", "spring", "summer"},
            ),
        )

        hose = ClothingClass(Rogue, "green_running_tights")

        if "green_athletic_shorts" in Rogue.Wardrobe.Clothes:
            hose.give_trait("seasonal", value = {"fall", "winter", "spring"})
            hose.give_trait("seasonal_replaced_by", value = {"green_athletic_shorts"})

        Outfits[-1].Clothes.update({
            "hair": ClothingClass(Rogue, "short_straight_ponytail_messy"),
            "bra": ClothingClass(Rogue, "black_sports_bra"), 
            "underwear": ClothingClass(Rogue, "yellow_cotton_panties"), 
            "hose": hose, 
            "socks": ClothingClass(Rogue, "black_ankle_socks"), 
            "footwear": ClothingClass(Rogue, "blackgreen_running_sneakers"),
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"),
        })

        # Hero (Chapter I)
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Hero (Chapter I)", 
                flags = {"hero", "fall", "winter", "spring", "summer"},
            ),
        )

        Outfits[-1].Clothes.update({
            "headband": ClothingClass(Rogue, "green_ch1_headband"),
            "bra": ClothingClass(Rogue, "black_sports_bra"), 
            "underwear": ClothingClass(Rogue, "yellow_cotton_panties"),
            "bodysuit": ClothingClass(Rogue, "greenyellow_ch1_suit"),
            "footwear": ClothingClass(Rogue, "yellow_ch1_boots"),
            "gloves": ClothingClass(Rogue, "yellow_ch1_gloves"), 
            "belt": ClothingClass(Rogue, "brown_utility_belt"),
            "jacket": ClothingClass(Rogue, "brown_bomber_jacket"),
        })

        # Swimsuit (One-Piece)
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Swimsuit (One-Piece)", 
                flags = {"swim", "fall", "winter", "spring", "summer"},
            ),
        )

        Outfits[-1].Clothes.update({
            "bodysuit": ClothingClass(Rogue, "greenyellow_sleeved_swimsuit"),
        })

        Outfits[-1].give_trait("no_bra")
        Outfits[-1].give_trait("no_underwear")

        # Swimsuit (Bikini)
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Swimsuit (Bikini)", 
                flags = {"swim", "fall", "winter", "spring", "summer"},
            ),
        )

        Outfits[-1].Clothes.update({
            "bra": ClothingClass(Rogue, "green_bikini_top"), 
            "underwear": ClothingClass(Rogue, "green_bikini_bottoms"),
        })

        # Datenight 1
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Datenight 1", 
                flags = {"public", "date", "fall", "spring", "summer"},
            ),
        )

        bra = ClothingClass(Rogue, "black_cami_tanktop")
        bra.give_trait("default")

        underwear = ClothingClass(Rogue, "yellow_cotton_panties")
        underwear.give_trait("default")

        Outfits[-1].Clothes.update({
            "bra": bra, 
            "underwear": underwear, 
            "hose": ClothingClass(Rogue, "black_sheer_pantyhose"), 
            "skirt": ClothingClass(Rogue, "black_leather_skirt"), 
            "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "top": ClothingClass(Rogue, "green_mesh_top"),
            "neck": ClothingClass(Rogue, "black_spiked_collar"), 
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"),
        })
        
        # Datenight 2
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Datenight 2", 
                flags = {"public", "date", "fall", "spring", "summer"},
            ),
        )

        underwear = ClothingClass(Rogue, "yellow_cotton_panties")
        underwear.give_trait("default")

        hose = ClothingClass(Rogue, "black_sheer_pantyhose")
        hose.give_trait("outdoors")
        hose.give_trait("seasonal", value = {"fall"})

        neck = ClothingClass(Rogue, "black_spiked_collar")
        neck.give_trait("optional")

        sleeves = ClothingClass(Rogue, "black_spiked_bracelets")
        sleeves.give_trait("optional")

        jacket = ClothingClass(Rogue, "brown_bomber_jacket")
        jacket.give_trait("outdoors")
        jacket.give_trait("seasonal", value = {"fall"})

        Outfits[-1].Clothes.update({
            "underwear": underwear, 
            "hose": hose,
            "footwear": ClothingClass(Rogue, "black_strap_pumps"),
            "dress": ClothingClass(Rogue, "yellow_summer_dress"),
            "neck": neck, 
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"), 
            "sleeves": sleeves,
            "jacket": jacket,
        })

        # Formal
        Outfits.append(OutfitClass(Rogue, "Formal"))

        Outfits[-1].Clothes.update({
            "underwear": ClothingClass(Rogue, "yellow_cotton_panties"),
            "footwear": ClothingClass(Rogue, "black_stiletto_heels"),
            "dress": ClothingClass(Rogue, "green_maxi_dress"),
            "gloves": ClothingClass(Rogue, "black_cutout_gloves"),
        })

        # Pajamas
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Pajamas", 
                flags = {"sleep", "fall", "winter", "spring", "summer"},
            ),
        )

        underwear = ClothingClass(Rogue, "yellow_cotton_panties")
        underwear.give_trait("default")

        Outfits[-1].Clothes.update({
            "bra": ClothingClass(Rogue, "black_cami_tanktop"), 
            "underwear": underwear,
        })

        # Lingerie 1
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Lingerie 1", 
                flags = {"sexy"},
            ),
        )

        Outfits[-1].Clothes.update({
            "bra": ClothingClass(Rogue, "green_lace_bra"), 
            "underwear": ClothingClass(Rogue, "green_lace_panties"), 
            "hose": ClothingClass(Rogue, "black_lace_garterbelt"), 
            "socks": ClothingClass(Rogue, "black_sheer_stockings"),
        })

        # Lingerie 2
        Outfits.append(
            OutfitClass(
                Rogue, 
                "Lingerie 2", 
                flags = {"sexy"},
            ),
        )

        Outfits[-1].Clothes.update({
            "underwear": ClothingClass(Rogue, "green_silk_thong"),
            "dress": ClothingClass(Rogue, "green_lace_nighty"),
        })

        Outfits[-1].give_trait("no_bra")
        
        # Nude
        Outfits.append(OutfitClass(Rogue, "Nude"))

        Outfits[-1].Clothes.update({})
                
        return Outfits