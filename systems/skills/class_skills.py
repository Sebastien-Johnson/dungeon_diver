from .skill_base import PhysSkills, MagSkills
import time
class WarriorSkills(PhysSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = {"1":"slash", "2":"vert_chop"}

    def slash(self, caster, target, cost=5, base_pow=1, accuracy=100):
        self.type_text(f"{caster.name} slashes the {target.name} with their weapon!")
        time.sleep(.5)
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.phys_player_status(caster, target)

    def vert_chop(self, caster, target, cost=8, base_pow=3, accuracy=85):
        self.type_text(f"{caster.name} sends a rising flash of steel through the {target.name}!")
        time.sleep(.5)
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.phys_player_status(caster, target)

class RangerSkills(PhysSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = {"1" : "arrow_shot"}

    def arrow_shot(self, caster, target, cost=2, base_pow=2, accuracy=100):
        self.type_text(f"{caster.name} fires an arrow at the {target.name}!")
        time.sleep(.5)
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.phys_player_status(caster, target)


class MageSkills(MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = {"1" : "mag_missile", "2": "fireball"}

    def mag_missile(self, caster, target, cost=5, base_pow=3, accuracy=100):
        self.type_text(f"{caster.name} cast a barrage of magical projectiles at the {target.name}!")
        time.sleep(.5)
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.mag_player_status(caster, target)

    def fireball(self, caster, target, cost=10, base_pow=8, accuracy=85):
        self.type_text(f"{caster.name} cares not for their surroundings and cast fireball at the {target.name}!")
        time.sleep(.5)
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.mag_player_status(caster, target)
        


class ClericSkills(MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = {"1" : "minor_heal", "2" : "smite"}
        
    def minor_heal(self, caster, target, cost=8, base_pow=4, accuracy=100):
        self.type_text(f"{caster.name} mends {caster.name}'s small wounds with holy light!")
        time.sleep(.5)
        self.mag_heal(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.mag_player_status(caster, target)

    def smite(self, caster, target, cost=6, base_pow=4, accuracy=100):
        self.type_text(f"{caster.name} imbues their weapon with holy light and strikes at the {target.name}!")
        time.sleep(.5)
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        time.sleep(.5)
        self.mag_player_status(caster, target)