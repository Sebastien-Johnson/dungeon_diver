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
        
    
    def __dir__(self, name):
        return getattr(self, name)
    
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
        self.type_text("Stats:", .02)
        attr_names = ["max_health", "phys_armor","mag_armor", "agility", "max_mana", "mag_pow", "max_stamina", "phys_pow"]
        for name in attr_names:
            self.type_text(f"{name}: {old_stats.__dir__(name)} -> {self.__dir__(name)}", .02)
        self.type_text("", .02)

    def lvl_up_once(self, initial_stats, unit_level):
        stat_names = ["max_health", "current_health", "phys_armor","mag_armor", "agility", "max_mana", "current_mana", "mag_pow", "max_stamina", "current_stamina", "phys_pow"]

        for name in stat_names:
            match initial_stats.__dir__(name):
                case 1:
                    if unit_level%5 == 0:
                        setattr(self, name, self.__dir__(name) + 1)
                        continue
                case 2:
                    if unit_level%4 == 0:
                        setattr(self, name, self.__dir__(name) + 1)
                        continue
                case 3:
                    if unit_level%3 == 0:
                        setattr(self, name, self.__dir__(name) + 1)
                        continue
                case 4:                   
                    if unit_level%2 == 0:
                        setattr(self, name, self.__dir__(name) + 1)
                        continue
                case 5:
                    if unit_level%1 == 0:
                        setattr(self, name, self.__dir__(name) + 1)
                        continue
            match name:
                case "current_mana":
                    if initial_stats.current_mana > 0:
                        setattr(self, name, self.__dir__(name) + 3)
                    continue
                case "max_mana":
                    if initial_stats.max_mana > 0:
                        setattr(self, name, self.__dir__(name) + 3)  
                    continue
                case "max_stamina":
                    if initial_stats.max_stamina > 0:
                        setattr(self, name, self.__dir__(name) + 3)
                    continue
                case "current_stamina":
                    if initial_stats.current_stamina > 0:
                        setattr(self, name, self.__dir__(name) + 3)
                    continue

    def lvl_up_to_lvl(self, unit_level):
        for l in range(unit_level+1):
            self.lvl_up_once(l)

    def show_item_stats(self):
        attr_names = ["max_health", "phys_armor","mag_armor", "agility", "max_mana", "mag_pow", "max_stamina", "phys_pow"]
        for name in attr_names:
            if self.__dir__(name) > 0:
                self.type_text(f"{name}: +{self.__dir__(name)}", .02)
            elif self.__dir__(name) < 0:
                self.type_text(f"{name}: {self.__dir__(name)}", .02)

    def take_potion(self, potion):
        self.current_health += potion.health
        self.current_mana += potion.mana
        self.current_stamina += potion.stamina
    
    def type_text(self, text_string, speed):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(speed)
        print("")
