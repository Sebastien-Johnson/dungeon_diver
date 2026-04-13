import random
from .item_libs.weapons import *
from .item_libs.armors import *


class LootMaker():
    def __init__(self):
        self.low_qualities = {"wood" : "musty birch", 
                              "metal" : "busted bronze", 
                              "fabric" : "crusty cotton", 
                              "leather" : "raunchy rawhide", 
                              "glass" : "cloudy"}
        self.med_qualities = {"wood" : "ok oak", 
                              "metal" : "aight iron", 
                              "fabric" : "lacking linen", 
                              "leather" : "lowkey leather", 
                              "glass" : "crystal clear"}
        self.high_qualities = {"wood" : "fine pine", 
                              "metal" : "sick steel", 
                              "fabric" : "smooth silk", 
                              "leather" : "sassy suede", 
                              "glass" : "fabulously flourescent"}
        
        self.metal_weapons = ["dagger", "sword", "two hander"]
        self.wood_weapons = ["shield", "wand", "staff", "bow"]
        self.glass_weapons = ["orb"]
        self.all_weapons = self.metal_weapons+self.wood_weapons+self.glass_weapons
        self.armor_materials = ["fabric", "leather", "metal"]
        self.armor_types = ["head", "chest", "arms", "legs"]
    

    def generate_loot(self, curr_dng_lvl):
        weapon_or_armor = random.choice([True, False])
        if weapon_or_armor:
            return self.generate_weapon(curr_dng_lvl)
        else:
            return self.generate_armor(curr_dng_lvl)

    def generate_weapon(self, curr_dng_lvl): 
        weapon_type = random.choice(self.all_weapons)
        material = self.find_weapon_material(weapon_type)
        quality_lvl = self.drop_rate(curr_dng_lvl)
        if quality_lvl == False:
            return 
        else:
            quality = quality_lvl[material]
        return self.forge_weapon(weapon_type, quality)
        
    def find_weapon_material(self, weapon_type):
        if weapon_type in self.metal_weapons:
            return "metal"
        elif weapon_type in self.wood_weapons:
            return "wood"
        elif weapon_type in self.glass_weapons:
            return "glass"
        else:
            print("Unknown weapon type!")
    
    def forge_weapon(self, weapon_type, quality):
        match weapon_type:
            case "dagger":
                return Dagger(quality)
            case "sword":
                return Sword(quality)
            case "two hander":
                return TwoHander(quality)
            case "shield":
                return Shield(quality)
            case "wand":
                return Wand(quality)
            case "staff":
                return Staff(quality)
            case "bow":
                return Bow(quality)
            case "orb":
                return Orb(quality)

        
    def generate_armor(self, curr_dng_lvl): 
        armor_type = random.choice(self.armor_types)
        material = random.choice(self.armor_materials)
        quality_lvl = self.drop_rate(curr_dng_lvl)
        if quality_lvl == False:
            return
        else:
            quality = quality_lvl[material]
        return self.forge_armor(armor_type, material, quality)

    def forge_armor(self, armor_type, material, quality):
        match material:
            case "metal":
                match armor_type:
                    case "head":
                        return HeavyHead(quality)
                    case "chest":
                        return HeavyChest(quality)
                    case "arms":
                        return HeavyArms(quality)
                    case "legs":
                        return HeavyLegs(quality)
            case "leather":
                match armor_type:
                    case "head":
                        return MediumHead(quality)
                    case "chest":
                        return MediumChest(quality)
                    case "arms":
                        return MediumArms(quality)
                    case "legs":
                        return MediumLegs(quality)
            case "fabric":
                match armor_type:
                    case "head":
                        return LightHead(quality)
                    case "chest":
                        return LightChest(quality)
                    case "arms":
                        return LightArms(quality)
                    case "legs":
                        return LightLegs(quality)
                

    def drop_rate(self, curr_dng_lvl):
        rate = random.randrange(100)
        low_rate = 60 - (curr_dng_lvl*.5)
        med_rate = 10 + (curr_dng_lvl*.75)
        high_rate = curr_dng_lvl *.1
        if rate <= high_rate:
            return self.high_qualities
        elif rate <= med_rate:
            return self.med_qualities
        elif rate <= low_rate:
            return self.low_qualities
        else:
            return False