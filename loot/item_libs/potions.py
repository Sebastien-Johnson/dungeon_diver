from items_base import Potion

class LessHealthPotion(Potion):
    def __init__(self, name="lesser health potion", item_type="potion", health=3, mana=0, stamina=0):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class GreatHealthPotion(Potion):
    def __init__(self, name="greater health potion", item_type="potion", health=6, mana=0, stamina=0):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class HighHealthPotion(Potion):
    def __init__(self, name="high health potion", item_type="potion", health=10, mana=0, stamina=0):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class LessManaPotion(Potion):
    def __init__(self, name="lesser mana potion", item_type="potion", health=0, mana=10, stamina=0):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class GreatManaPotion(Potion):
    def __init__(self, name="greater mana potion", item_type="potion", health=0, mana=15, stamina=0):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class HighManaPotion(Potion):
    def __init__(self, name="high mana potion", item_type="potion", health=0, mana=20, stamina=0):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class LessStaminaPotion(Potion):
    def __init__(self, name="lesser stamina potion", item_type="potion", health=0, mana=0, stamina=10):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class GreatStaminaPotion(Potion):
    def __init__(self, name="greater stamina potion", item_type="potion", health=0, mana=0, stamina=15):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina

class HighStaminaPotion(Potion):
    def __init__(self, name="high stamina potion", item_type="potion", health=0, mana=0, stamina=20):
        super().__init__(name, item_type, health, mana, stamina)
        self.name = name
        self.item_type = item_type
        self.health = health
        self.mana = mana
        self.stamina = stamina