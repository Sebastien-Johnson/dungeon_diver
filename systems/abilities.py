class Ability():
    def __init__(self):
        self.description = "" 

    def attack_skill(self, cost, caster, target, base_pow, pow_type):
        if pow_type == "phys_pow":
            if caster.base_stats.current_stamina >= cost:
                attack_power = base_pow + caster.base_stats.phys_pow
                target.take_phys_damage(attack_power)
            else:
                print("Not enough stamina!")
        else:
            if caster.base_stats.current_mana >= cost:
                attack_power = base_pow + caster.base_stats.mag_pow
                target.take_mag_damage(attack_power)
            else:
                print("Not enough mana!")

    def heal_skill(self, cost, caster, target, base_pow, pow_type):
        if pow_type == "phys_pow":
            if caster.base_stats.current_stamina >= cost:
                heal_power = base_pow + caster.base_stats.phys_pow
                target.restore_health(heal_power)
            else:
                print("Not enough stamina!")
        else:
            if caster.base_stats.current_mana >= cost:
                heal_power = base_pow + caster.base_stats.mag_pow
                target.restore_health(heal_power)
            else:
                print("Not enough mana!")
        

class Slash(Ability):
    def __init__(self):
        super().__init__()
        self.description = " slashes with their weapon!"

class MagicMissile(Ability): 
    def __init__(self):
        super().__init__()
        self.description = " cast a barrage of magical projectiles!" 

class ArrowShot(Ability):
    def __init__(self):
        super().__init__()
        self.description = " fires an arrow of great precision!"  

class MinorHeal(Ability):
    def __init__(self):
        super().__init__()
        self.description = " channels holy light, mending small wounds!"

class Smite(Ability):
    def __init__(self):
        super().__init__()
        self.description = " imbues their weapon with holy might and strikes!"