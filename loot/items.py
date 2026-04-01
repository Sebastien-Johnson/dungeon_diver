from systems.stats import Stats

class Item():
    def __init__(self, name, item_type):
        self.name = name
        self.type = item_type
        self.stats = Stats()


class Potion(Item):
    def __init__(self, name, item_type):
        super().__init__(name, item_type)
        self.item_type = "Potion"

class Equipment(Item):
    def __init__(self, name, item_type, hands, enchantment, class_lock):
        super().__init__(name, item_type)
        self.hands = hands
        self.enchantment = enchantment
        self.class_lock = class_lock

class Weapon(Equipment):
    def __init__(self, name, item_type, hands, enchantment, class_lock):
        super().__init__(name, item_type, hands, enchantment, class_lock)
        self.item_type = "weapon"

class HeadPiece(Equipment):
    def __init__(self, name, item_type, hands, enchantment, class_lock):
        super().__init__(name, item_type, hands, enchantment, class_lock)
        self.item_type = "head"

class ChestPiece(Equipment):
    def __init__(self, name, item_type, hands, enchantment, class_lock):
        super().__init__(name, item_type, hands, enchantment, class_lock)
        self.item_type = "chest"

class ArmPiece(Equipment):
    def __init__(self, name, item_type, hands, enchantment, class_lock):
        super().__init__(name, item_type, hands, enchantment, class_lock)
        self.item_type = "arms"

class LegPiece(Equipment):
    def __init__(self, name, item_type, hands, enchantment, class_lock):
        super().__init__(name, item_type, hands, enchantment, class_lock)
        self.item_type = "legs"



    


