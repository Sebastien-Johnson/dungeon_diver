from systems.stats import Stats

class Item():
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type
        self.stats = Stats()


class Potion(Item):
    def __init__(self, name, item_type, health, mana, stamina):
        super().__init__(name, item_type)
        self.item_type = "Potion"
        self.health = health
        self.mana = mana
        self.stamina = stamina

class Equipment(Item):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality

    def choose_metal_quality(self, low, medium, high, given_quality):
        match given_quality:
            case "busted bronze":
                return low
            case "aight iron":
                return medium
            case "sick steel":
                return high
            
    def choose_wood_quality(self, low, medium, high, given_quality):
        match given_quality:
            case "musty birch":
                return low
            case "ok oak":
                return medium
            case "fine pine":
                return high

    def choose_linen_quality(self, low, medium, high, given_quality):
        match given_quality:
            case "crusty cotton":
                return low
            case "linen":
                return medium
            case "silk":
                return high

    def choose_leather_quality(self, low, medium, high, given_quality):
        match given_quality:
            case "raunchy rawhide":
                return low
            case "lowkey leather":
                return medium
            case "sassy suede":
                return high
            
    def choose_orb_quality(self, low, medium, high, given_quality):
        match given_quality:
            case "cloudy":
                return low
            case "clear":
                return medium
            case "flourescent":
                return high

class Weapon(Equipment):
    def __init__(self, quality, name, hands):
        super().__init__(quality, name, hands)
        self.hands = hands

class HeadPiece(Equipment):
    def __init__(self, quality, name, item_type):
        super().__init__(name, item_type, quality)
        

class ChestPiece(Equipment):
    def __init__(self, quality, name, item_type):
        super().__init__(name, item_type, quality)
        

class ArmPiece(Equipment):
    def __init__(self, quality, name, item_type):
        super().__init__(name, item_type, quality)
        

class LegPiece(Equipment):
    def __init__(self, quality, name, item_type):
        super().__init__(name, item_type, quality)
        



    


