from systems.stats import Stats
from loot.equipment import Inventory
from systems.player_races import Race

class Unit():
    def __init__(self, name, race, unit_class, lvl=1):
        self.stats = Stats()
        self.inventory = Inventory()
        self.race = Race()
        self.unit_class = unit_class
        self.lvl = lvl
        self.abilities = {}
        self.current_xp = int()
        self.xp_to_lvl = int()
        self.xp_val = int()



class Player(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)

class Monster(Unit):
    def __init__(self, name, race, unit_class, lvl):
        super().__init__(name, race, unit_class, lvl)

class Warrior(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.stats = Stats(4, 4, 2, 3, None, None, 30, 3)
        self.current_xp = 0
        
class Mage(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.stats = Stats(2, 2, 2, 1, 30, 9, None, None)
        self.current_xp = 0

class Cleric(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.stats = Stats(3, 3, 3, 2, 30, 5, None, None) 
        self.current_xp = 0

class Ranger(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.stats = Stats(2, 2, 2, 5, None, None, 30, 5) 
        self.current_xp = 0