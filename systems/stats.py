import sys
from units import Player, Monster

class Stats():
    def __init__(self, max_health=0, phys_armor=0, mag_armor=0, agility=0, max_mana=None, mag_pow=None, max_stamina=None, phys_pow=None):
        self.max_health = max_health
        self.current_health = max_health
        self.phys_armor = phys_armor
        self.mag_armor = mag_armor
        self.agility = agility
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.mag_pow = mag_pow
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina
        self.phys_pow = phys_pow

    def add_stats(self, new_stats):
        self.max_health += new_stats.max_health
        self.phys_armor += new_stats.phys_armor
        self.mag_armor += new_stats.mag_armor
        self.agility += new_stats.agility
        self.check_has_stat("max_mana", new_stats.max_mana)
        self.check_has_stat("mag_pow", new_stats.mag_pow)
        self.check_has_stat("max_stamina", new_stats.max_stamina)
        self.check_has_stat("phys_pow", new_stats.phys_pow)

    def check_has_stat(self, stat_name, stat):
        if self.stat_name:
            self.stat += stat

    def use_stam(self, cost):
        if cost <= self.current_stamina:
            self.current_stamina -= cost
        else:
            print("Not enough stamina!")
    
    def restore_stam(self, recovery):
        recovered_stam = recovery + self.current_stamina
        if recovered_stam >= self.max_stamina:
            self.current_stamina = self.max_stamina
        else:
            self.current_stamina = recovered_stam

    def use_mana(self, cost):
        if cost <= self.current_mana:
            self.current_mana -= cost
        else:
            print("Not enough mana!")

    def restore_mana(self, recovery):
        recovered_mana = recovery + self.current_mana
        if recovered_mana >= self.max_mana:
            self.current_mana = self.max_mana
        else:
            self.current_smana = recovered_mana

    def restore_health(self, recovery):
        recovered_health = recovery + self.current_health
        if recovered_health >= self.max_health:
            self.current_health = self.max_health
        else:
            self.current_health = recovered_health

    def rest(self):
        self.restore_mana(self.max_mana)
        self.restore_stam(self.max_stamina)
        self.restore_health(self.max_health)
        

    def take_phys_damage(self, damage, unit):
        effective_dmg = damage - self.phys_armor
        self.current_health -= effective_dmg
        if self.current_health <= 0 & unit == Player():
            sys.exit("You died...")
        elif self.current_health <= 0 & unit == Monster():
            return unit.xp_val

    def take_mag_damage(self, damage, unit):
        effective_dmg = damage - self.mag_armor
        self.current_health -= effective_dmg
        if self.current_health <= 0 & unit == Player():
            sys.exit("You died...")
        elif self.current_health <= 0 & unit == Monster():
            return unit.xp_val