from classes import *
from loot.equipment import Inventory
from systems.player_races import Race

class Unit():
    def __init__(self, unit_class, name=str, race=Race, lvl=1):
        self.name = name
        self.race = race
        self.unit_class = unit_class
        self.lvl = lvl
        self.abilities = unit_class.abilities
        self.inventory = Inventory()


class Player(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.current_xp = int()
        self.xp_to_lvl = int()
        self.stats = unit_class.stats 

class Monster(Unit):
    def __init__(self, name, race, unit_class, lvl):
        super().__init__(name, race, unit_class, lvl)
        self.xp_val = int()
        self.stats = Stats()
