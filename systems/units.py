from loot.equipment import Inventory
from .lvls_xp import Leveling
import sys

class Unit():
    def __init__(self,  name, race, unit_class, lvl=1):
        self.name = name
        self.race = race
        self.unit_class = unit_class
        self.leveling = Leveling()
        self.current_lvl = self.leveling.current_lvl
        self.inventory = Inventory()
    
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


class Player(Unit):
    def __init__(self, name, race, unit_class, lvl=1):
        super().__init__(name, race, unit_class, lvl)
        self.name = name
        self.current_xp = int()
        self.xp_to_lvl = int()
        self.base_stats = unit_class.stats
        self.base_stats.add_stats(race.stat_bonuses)
        self.skills = unit_class.skills

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

class Monster(Unit):
    def __init__(self, race, unit_class, lvl):
        super().__init__(race, unit_class, lvl)
        self.name = race.name
        self.xp_val = int()
        self.base_stats = race.stats
        self.base_stats.add_stats(unit_class.base_stats)
        self.skills = unit_class.skills

    def take_phys_damage(self, damage, caster):
        effective_dmg = damage - self.base_stats.phys_armor
        self.base_stats.current_health -= effective_dmg
        if self.base_stats.current_health <= 0:
            caster.leveling.xp_bar += self.xp_val

    def take_mag_damage(self, damage, caster):
        effective_dmg = damage - self.base_stats.mag_armor
        self.base_stats.current_health -= effective_dmg
        if self.base_stats.current_health <= 0:
            caster.leveling.xp_bar += self.xp_val

