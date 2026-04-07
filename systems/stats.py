import time

class Stats():
    def __init__(self, max_health=0, phys_armor=0, mag_armor=0, agility=0, max_mana=0, mag_pow=0, max_stamina=0, phys_pow=0):
        self.max_health = max_health
        self.current_health = self.max_health
        self.phys_armor = phys_armor
        self.mag_armor = mag_armor
        self.agility = agility
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.mag_pow = mag_pow
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina
        self.phys_pow = phys_pow 
        self.all_stats = {"HP" : self.max_health,
                          "Physical Armor" : self.phys_armor, 
                          "Magic Armor" : self.mag_armor, 
                           "Agility" : self.agility, 
                           "Mana" : self.max_mana, 
                           "Magic Power" : self.mag_pow, 
                           "Stamina" : self.max_stamina, 
                           "Physical Power" : self.phys_pow}

    def add_stats(self, new_stats):
        self.max_health += new_stats.max_health
        self.current_health += new_stats.max_health
        self.phys_armor += new_stats.phys_armor
        self.mag_armor += new_stats.mag_armor
        self.agility += new_stats.agility
        self.max_mana += new_stats.max_mana
        self.current_mana += new_stats.max_mana
        self.mag_pow += new_stats.mag_pow
        self.max_stamina += new_stats.max_stamina
        self.current_stamina += new_stats.max_stamina
        self.phys_pow += new_stats.phys_pow
    
    def remove_stats(self, old_stats):
        self.max_health -= old_stats.max_health
        self.current_health -= old_stats.max_health
        self.phys_armor -= old_stats.phys_armor
        self.mag_armor -= old_stats.mag_armor
        self.agility -= old_stats.agility
        self.max_mana -= old_stats.max_mana
        self.current_mana -= old_stats.max_mana
        self.mag_pow -= old_stats.mag_pow
        self.max_stamina -= old_stats.max_stamina
        self.current_stamina -= old_stats.max_stamina
        self.phys_pow -= old_stats.phys_pow

    def show_stat_update(self, old_stats):
        for key, value in old_stats.all_stats:
            self.type_text(f"{key}: {value} -> {self.all_stats[value]}", .02)

    def take_potion(self, potion):
        self.current_health += potion.health
        self.current_mana += potion.mana
        self.current_stamina += potion.stamina
    
    def type_text(self, text_string, speed):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(speed)
        print("")
        
    