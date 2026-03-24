from .skill_base import PhysSkills, MagSkills

class WarriorSkills(PhysSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = ["slash"]

    def slash(self, caster, target, cost=5, base_pow=1, accuracy=100):
        print(f"{caster.name} slashes the {target.name} with their weapon!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

class RangerSkills(PhysSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.arrow_shot]

    def arrow_shot(self, caster, target, cost=2, base_pow=2, accuracy=100):
        print(f"{caster.name} fires an arrow at the {target.name}!")


class MageSkills(MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.mag_missile]

    def mag_missile(self, caster, target, cost=8, base_pow=4, accuracy=100):
        print(f"{caster.name} cast a barrage of magical projectiles at the {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)


class ClericSkills(MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.minor_heal, self.smite]
        
    def minor_heal(self, caster, target, cost=8, base_pow=4, accuracy=100):
        print(f"{caster.name} mends {target.name}'s small wounds with holy light!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)

    def smite(self, caster, target, cost=8, base_pow=4, accuracy=100):
        print(f"{caster.name} imbues their weapon with holy light and strikes at the {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)