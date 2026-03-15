from classes import *
from loot.equipment import Inventory
from systems.player_races import Race
import sys

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
        self.base_stats = unit_class.stats.add_stats(race.stat_bonuses) 

    def use_stam(self, cost):
        if cost <= self.base_stats.current_stamina:
            self.base_stats.current_stamina -= cost
        else:
            print("Not enough stamina!")
    
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
            print("Not enough mana!")

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

    def rest(self):
        self.restore_mana(self.base_stats.max_mana)
        self.restore_stam(self.base_stats.max_stamina)
        self.restore_health(self.base_stats.max_health)
        

    def take_phys_damage(self, damage):
        effective_dmg = damage - self.base_stats.phys_armor
        self.base_stats.current_health -= effective_dmg
        if self.base_stats.current_health <= 0:
            sys.exit("You died...")

    def take_mag_damage(self, damage):
        effective_dmg = damage - self.base_stats.mag_armor
        self.base_stats.current_health -= effective_dmg
        if self.base_stats.current_health <= 0:
            sys.exit("You died...")
        elif self.base_stats.current_health <= 0 & unit == Monster():
            return unit.xp_val

class Monster(Unit):
    def __init__(self, name, race, unit_class, lvl):
        super().__init__(name, race, unit_class, lvl)
        self.xp_val = int()
        self.base_stats = unit_class.stats.add_stats(race.base_stats)

    def use_stam(self, cost):
        if cost <= self.base_stats.current_stamina:
            self.base_stats.current_stamina -= cost
        else:
            print("Not enough stamina!")
    
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
            print("Not enough mana!")

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

    def rest(self):
        self.restore_mana(self.base_stats.max_mana)
        self.restore_stam(self.base_stats.max_stamina)
        self.restore_health(self.base_stats.max_health)
        

    def take_phys_damage(self, damage):
        effective_dmg = damage - self.base_stats.phys_armor
        self.base_stats.current_health -= effective_dmg
        if self.base_stats.current_health <= 0:
            return self.xp_val

    def take_mag_damage(self, damage):
        effective_dmg = damage - self.base_stats.mag_armor
        self.base_stats.current_health -= effective_dmg
        if self.base_stats.current_health <= 0:
            return self.xp_val

