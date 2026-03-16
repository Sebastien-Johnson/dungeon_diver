from skill_base import PhysSkills, MagSkills

class WarriorSkills(PhysSkills):
    def __init__(self):
        super().__init__()

    def slash(self, caster, target, cost=5, base_pow=1, accuracy=100):
        print(f"{caster.name} slashes {target.name} with their weapon!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

class RangerSkills(PhysSkills):
    def __init__(self):
        super().__init__()

    def arrow_shot(self, caster, target, cost=2, base_pow=2, accuracy=100):
        print(f"{caster.name} fires an arrow {target.name}!")


class MageSkills(MagSkills):
    def __init__(self):
        super().__init__()

    def mag_missle(self, caster, target, cost=8, base_pow=4, accuracy=100):
        print(f"{caster.name} cast a barrage of magical projectiles at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)


class ClericSkills(MagSkills):
    def __init__(self):
        super().__init__()

    def minor_heal(self, caster, target, cost=8, base_pow=4, accuracy=100):
        print(f"{caster.name} mends {target.name}'s small wounds with holy light!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)

    def smite(self, caster, target, cost=8, base_pow=4, accuracy=100):
        print(f"{caster.name} imbues their weapon with holy light and strikes at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)