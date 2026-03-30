import random, time, sys
from systems.units import Monster, Player


class Skills():
    def __init__(self):
        self.description = "" 

    def check_accuracy(self, accuracy):
        acc_check = random.randrange(1, 100)
        if acc_check <= accuracy:
            return True
        else:
            print("They missed!")
            return False
        
    def check_stamina(self, caster, cost):
        if caster.base_stats.current_stamina >= cost:
            caster.base_stats.current_stamina -= cost
            return True
        else:
            print("Not enough stamina!")

    def check_mana(self, caster, cost):
        if caster.base_stats.current_mana >= cost:
            caster.base_stats.current_mana -= cost
            return True
        else:
            print("Not enough mana!")
        
    def calc_phys_power(self, caster, base_pow):
        return base_pow + caster.base_stats.phys_pow
        
    
    def calc_mag_power(self, caster, base_pow):
        return base_pow + caster.base_stats.mag_pow
    
    def check_if_slain(self, caster, target):
        if target.base_stats.current_health <= 0:
            time.sleep(1)
            if type(target) == Monster:
                    print(f"The {target.name} has been slain!")
                    time.sleep(1)
                    print(f"{caster.name} gained {target.xp_val} experience points!\n")
                    caster.leveling.add_xp(target.xp_val)
            if type(target) == Player:
                sys.exit("You died...")
                

    def phys_player_status(self, caster, target):
        print(f"{caster.name} health remaining: {caster.base_stats.current_health}/{caster.base_stats.max_health}, stamina remaining {caster.base_stats.current_stamina}/{caster.base_stats.max_stamina}")
        print(f"{target.name} health remaining: {max(target.base_stats.current_health,0)}/{target.base_stats.max_health}\n")

    def mag_player_status(self, caster, target):
        print(f"{caster.name} health remaining: {caster.base_stats.current_health}/{caster.base_stats.max_health}, mana remaining {caster.base_stats.current_mana}/{caster.base_stats.max_mana}")
        print(f"{target.name} health remaining: {max(target.base_stats.current_health,0)}/{target.base_stats.max_health}\n")
    
    def monster_status(self, caster, target):
        print(f"{target.name} health remaining: {target.base_stats.current_health}/{target.base_stats.max_health}")
        print(f"{caster.name} health remaining: {caster.base_stats.current_health}/{caster.base_stats.max_health}\n")
        
           
class PhysSkills(Skills):
    def __init__(self):
        super().__init__()  

    def phys_attack(self, caster, target, cost, base_pow, accuracy):
        if self.check_stamina(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.take_phys_damage(self.calc_phys_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health
                time.sleep(1)
                print(f"{caster.name} did {hp2} physical damage to {target.name}!\n")
                self.check_if_slain(caster, target)
                return True
    
    def phys_heal(self, caster, target, cost, base_pow, accuracy):
        if self.check_stamina(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.restore_health(self.calc_phys_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health 
                time.sleep(1)
                print(f"{target.name} restored {hp2} health points!")
                return True   

class MagSkills(Skills):
    def __init__(self):
        super().__init__()
    
    def mag_attack(self, caster, target, cost, base_pow, accuracy):
        if self.check_mana(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.take_mag_damage(self.calc_mag_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health
                time.sleep(1)
                print(f"{caster.name} did {hp2} magic damage to {target.name}!!")
                self.check_if_slain(caster, target)
                return True
    
    def mag_heal(self, caster, target, cost, base_pow, accuracy):
        if self.check_mana(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.restore_health(self.calc_mag_power)
                hp2 = hp1 - target.base_stats.current_health
                time.sleep(1)
                print(f"{target.name} restored {hp2} health points!") 
                return True


