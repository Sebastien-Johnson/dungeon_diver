from loot.inventory import UnitInventory
from ..lvls_xp import Leveling
from loot.make_loot import LootMaker
import time
import math


class Unit():
    def __init__(self,  name, race, unit_class, lvl=1):
        self.name = name
        self.race = race
        self.unit_class = unit_class
        self.leveling = Leveling()
        self.current_lvl = self.leveling.current_lvl
        self.inventory = UnitInventory()
    
    def use_stam(self, cost):
        if cost <= self.base_stats.current_stamina:
            self.base_stats.current_stamina -= cost
        else:
            self.type_text("Not enough stamina!")
    
    def restore_stam(self, recovery):
        recovered_stam = recovery + self.base_stats.current_stamina
        if recovered_stam >= self.base_stats.max_stamina:
            self.base_stats.current_stamina = self.base_stats.max_stamina
        else:
            self.base_stats.current_stamina = recovered_stam

    def use_mana(self, cost):
        if cost <= self.base_stats.current_mana:
            self.base_stats.current_mana -= cost
        else:
            self.type_text("Not enough mana!")

    def restore_mana(self, recovery):
        recovered_mana = recovery + self.base_stats.current_mana
        if recovered_mana >= self.base_stats.max_mana:
            self.base_stats.current_mana = self.base_stats.max_mana
        else:
            self.base_stats.current_mana = recovered_mana

    def restore_health(self, recovery):
        recovered_health = recovery + self.base_stats.current_health
        if recovered_health >= self.base_stats.max_health:
            self.base_stats.current_health = self.base_stats.max_health
        else:
            self.base_stats.current_health = recovered_health

    def short_rest(self, curr_dng_lvl):
        initial_hp = self.base_stats.current_health
        self.restore_health(1)
        self.type_text(f"HP: {initial_hp} -> {self.base_stats.current_health}")
        restore = 5 + math.floor(curr_dng_lvl/10)
        if self.base_stats.max_mana > 0:
            initial_mana = self.base_stats.current_mana
            self.restore_mana(restore)
            self.type_text(f"Mana: {initial_mana} -> {self.base_stats.current_mana}")
        if self.base_stats.max_stamina > 0:
            initial_stamina = self.base_stats.current_stamina
            self.restore_stam(restore)
            self.type_text(f"Stamina: {initial_stamina} -> {self.base_stats.current_stamina}")

    def long_rest(self):
        self.restore_mana(self.base_stats.max_mana)
        self.restore_stam(self.base_stats.max_stamina)
        self.restore_health(self.base_stats.max_health)

    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")


class Player(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.name = name
        self.current_xp = self.leveling.xp_bar.current_xp
        self.xp_to_lvl = int()
        self.initial_stats = unit_class.stats #static lvl 1 stats
        self.base_stats = self.initial_stats #scaling stats with flat racial & equipment bonuses
        self.total_stats = self.base_stats #add equipment & race bonuses
        self.total_stats.add_stats(race.stat_bonuses)
        self.skills = unit_class.skills

    def take_phys_damage(self, damage): 
        effective_dmg = damage - self.base_stats.phys_armor
        self.base_stats.current_health -= effective_dmg

    def take_mag_damage(self, damage):
        effective_dmg = damage - self.base_stats.mag_armor
        self.base_stats.current_health -= effective_dmg

        

class Monster(Unit):
    def __init__(self, race, unit_class=None, lvl=1):
        super().__init__(race, unit_class, lvl)
        self.name = race.name
        self.xp_val = race.xp_val
        self.base_stats = race.base_stats
        self.skills = race.skills
        self.unit_class = unit_class
        if self.unit_class:
            self.base_stats.add_stats(unit_class.base_stats)
            self.name = unit_class.name + " " + race.name

    def take_phys_damage(self, damage):
        effective_dmg = damage - self.base_stats.phys_armor
        self.base_stats.current_health -= effective_dmg
        

    def take_mag_damage(self, damage):
        effective_dmg = damage - self.base_stats.mag_armor
        self.base_stats.current_health -= effective_dmg

    def add_loot_equipment(self, curr_dng_lvl):
        dungeon_spoils = LootMaker()
        loot = dungeon_spoils.generate_loot(curr_dng_lvl)
        self.inventory.equip_item(loot, self)