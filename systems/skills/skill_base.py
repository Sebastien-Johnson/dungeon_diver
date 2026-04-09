import random, time, sys
from systems.units.units_base import Monster, Player


class Skills():
    def __init__(self):
        self.description = "" 

    def check_accuracy(self, accuracy):
        acc_check = random.randrange(1, 100)
        if acc_check <= accuracy:
            return True
        else:
            self.type_text("They missed!")
            return False
        
    def check_stamina(self, caster, cost):
        if caster.base_stats.current_stamina >= cost:
            caster.base_stats.current_stamina -= cost
            return True
        else:
            self.type_text("Not enough stamina!")

    def check_mana(self, caster, cost):
        if caster.base_stats.current_mana >= cost:
            caster.base_stats.current_mana -= cost
            return True
        else:
            self.type_text("Not enough mana!")
        
    def calc_phys_power(self, caster, base_pow):
        return base_pow + caster.base_stats.phys_pow
        
    
    def calc_mag_power(self, caster, base_pow):
        return base_pow + caster.base_stats.mag_pow
    
    def check_if_slain(self, caster, target):
        if target.base_stats.current_health <= 0: 
            time.sleep(1)
            if type(target) == Monster:
                    self.type_text(f"The {target.name} has been slain!")
                    time.sleep(1)
                    self.type_text(f"{caster.name} gained {target.xp_val} experience points!\n")
                    caster.leveling.add_xp(caster, target.xp_val) 
                    
            if type(target) == Player:
                sys.exit("You died...")

    def check_if_loot(self, caster, target):
        for loot in target.inventory.equiped:
            self.type_text(f"{target.name} had a {loot.name}!")
            self.type_text("Choose to equip? (y/n)")
            response = input()
            if response in ["yes", "y"]:
                caster.inventory.equip_item(loot)
                self.type_text(f"{loot.name} equiped!")
                

    def phys_player_status(self, caster, target):
        self.type_text(f"{caster.name} health remaining: {caster.base_stats.current_health}/{caster.base_stats.max_health}, stamina remaining {caster.base_stats.current_stamina}/{caster.base_stats.max_stamina}")
        if target.base_stats.current_health > 0:
            self.type_text(f"{target.name} health remaining: {max(target.base_stats.current_health,0)}/{target.base_stats.max_health}\n")

    def mag_player_status(self, caster, target):
        self.type_text(f"{caster.name} health remaining: {caster.base_stats.current_health}/{caster.base_stats.max_health}, mana remaining {caster.base_stats.current_mana}/{caster.base_stats.max_mana}")
        self.type_text(f"{target.name} health remaining: {max(target.base_stats.current_health,0)}/{target.base_stats.max_health}\n")
    
    def monster_status(self, caster, target):
        self.type_text(f"{target.name} health remaining: {target.base_stats.current_health}/{target.base_stats.max_health}")
        self.type_text(f"{caster.name} health remaining: {caster.base_stats.current_health}/{caster.base_stats.max_health}\n")
    
    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")
        
           
class PhysSkills(Skills):
    def __init__(self):
        super().__init__()  

    def phys_attack(self, caster, target, cost, base_pow, accuracy):
        if self.check_stamina(caster, cost):
            if self.check_accuracy(accuracy-target.base_stats.agility):
                hp1 = target.base_stats.current_health
                target.take_phys_damage(self.calc_phys_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health
                time.sleep(1)
                self.type_text(f"{caster.name} did {hp2} physical damage to {target.name}!\n")
                self.check_if_slain(caster, target)
                return True
    
    def phys_heal(self, caster, target, cost, base_pow, accuracy):
        if self.check_stamina(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.restore_health(self.calc_phys_power(caster, base_pow))
                hp2 = target.base_stats.current_health - hp1
                time.sleep(1)
                self.type_text(f"{target.name} restored {hp2} health points!")
                return True   

class MagSkills(Skills):
    def __init__(self):
        super().__init__()
    
    def mag_attack(self, caster, target, cost, base_pow, accuracy):
        if self.check_mana(caster, cost):
            if self.check_accuracy(accuracy-target.base_stats.agility):
                hp1 = target.base_stats.current_health
                target.take_mag_damage(self.calc_mag_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health
                time.sleep(1)
                self.type_text(f"{caster.name} did {hp2} magic damage to {target.name}!!")
                self.check_if_slain(caster, target)
                return True
    
    def mag_heal(self, caster, target, cost, base_pow, accuracy):
        if self.check_mana(caster, cost):
            if self.check_accuracy(accuracy-target.base_stats.agility):
                hp1 = target.base_stats.current_health
                target.restore_health(self.calc_mag_power)
                hp2 = hp1 - target.base_stats.current_health
                time.sleep(1)
                self.type_text(f"{target.name} restored {hp2} health points!") 
                return True
            
    


