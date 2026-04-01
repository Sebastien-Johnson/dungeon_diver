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

class Weapon(Equipment):
    def __init__(self, name, item_type, hands, quality):
        super().__init__(name, item_type, hands, quality)
        self.hands = hands

class HeadPiece(Equipment):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type, quality)
        self.item_type = "head"

class ChestPiece(Equipment):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type, quality)
        self.item_type = "chest"

class ArmPiece(Equipment):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type, quality)
        self.item_type = "arms"

class LegPiece(Equipment):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type, quality)
        self.item_type = "legs"



    


