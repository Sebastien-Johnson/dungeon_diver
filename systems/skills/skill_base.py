import random

class Skills():
    def __init__(self):
        self.description = "" 

    def check_accuracy(self, accuracy):
        acc_check = random.randrange(1, 100)
        if acc_check <= accuracy:
            return True
        else:
            print("You missed!")
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
    
           
class PhysSkills(Skills):
    def __init__(self):
        super().__init__()  

    def phys_attack(self, caster, target, cost, base_pow, accuracy):
        if self.check_stamina(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.take_phys_damage(self.calc_phys_power(caster, base_pow), caster)
                hp2 = hp1 - target.base_stats.current_health
                print(f"{caster.name} did {hp2} physical damage to {target.name}!\n")
                return True
    
    def phys_heal(self, cost, caster, target, base_pow, accuracy):
        if self.check_stamina(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.restore_health(self.calc_phys_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health 
                print(f"{target.name} restored {hp2} health points!")
                return True   

class MagSkills(Skills):
    def __init__(self):
        super().__init__()
    
    def mag_attack(self, cost, caster, target, base_pow, accuracy):
        if self.check_mana(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.take_mag_damage(self.calc_mag_power(caster, base_pow))
                hp2 = hp1 - target.base_stats.current_health
                print(f"{caster.name} did {hp2} magic damage tp {target.name}!")
                return True
    
    def mag_heal(self, cost, caster, target, base_pow, accuracy):
        if self.check_mana(caster, cost):
            if self.check_accuracy(accuracy):
                hp1 = target.base_stats.current_health
                target.restore_health(self.calc_mag_power)
                hp2 = hp1 - target.base_stats.current_health
                print(f"{target.name} restored {hp2} health points!") 
                return True


