from .skill_base import PhysSkills, MagSkills

class SlimeSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()
    
        self.skill_list = [self.absorb]
    
    def absorb(self, caster, target, cost=5, base_pow=5, accuracy=75):
        print(f"{caster.name} learches at {target.name} to leach their essence!")
        if self.phys_attack(caster, target, cost, base_pow, accuracy):
            self.phys_attack(caster, target, cost, base_pow, 100)
            self.phys_heal(caster, caster, base_pow, 100)

class BatSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()

        self.skills_list = [self.scratch, self.vamp_bite]

    def scratch(self, caster, target, cost=5, base_pow=1, accuracy=85):
        print(f"{caster.name} scratches {target.name} with their claws!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

    def vamp_bite(self, caster, target, cost=5, base_pow=5, accuracy=75):
        print(f"{caster.name} learches at {target.name} to leach their essence!")
        if self.phys_attack(caster, target, cost, base_pow, accuracy):
            self.phys_attack(caster, target, cost, base_pow, 100)
            self.phys_heal(caster, caster, base_pow, 100)

class GoblinSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.stab, self.sling]

    def stab(self, caster, target, cost=5, base_pow=1, accuracy=95):
        print(f"{caster.name} stabs at {target.name} with their {caster.inventory.weapon}!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

    def sling(self, caster, target, cost=5, base_pow=2, accuracy=80):
        print(f"{caster.name} slings a rock at {target.name}!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
    

class DirewolfSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()
    
        self.skill_list = [self.bite]

    def bite(self, caster, target, cost=5, base_pow=3, accuracy=80):
        print(f"{caster.name} lunges to rend {target.name}'s flesh!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

class KoboldSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.hot_breath, self.bite, self.slash]
    
    def hot_breath(self, caster, target, cost=5, base_pow=4, accuracy=60):
        print(f"{caster.name} sends a wave of fire at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)

    def bite(self, caster, target, cost=5, base_pow=4, accuracy=80):
        print(f"{caster.name} lunges to rend {target.name}'s flesh!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
    
    def slash(self, caster, target, cost=5, base_pow=1, accuracy=95):
        print(f"{caster.name} slashes at {target.name} with their {caster.inventory.weapon}!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

class TrollSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()
    
        self.skill_list = [self.skull_splitter]

    def skull_splitter(self, caster, target, cost=8, base_pow=6, accuracy=60):
        print(f"{caster.name} drops their {caster.inventory.weapon} down at {target.name}'s with all their might!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

class GiantSkills(TrollSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.skull_splitter, self.boulder_drop, self.earthquake]

    def boulder_drop(self, caster, target, cost=20, base_pow=10, accuracy=80):
        print(f"{caster.name} RKO's a boulder over {target.name}'s head!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)

    def earthquake(self, caster, target, cost=30, base_pow=10, accuracy=100):
        print(f"{caster.name} splits the earth beneath {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)

class DragonSkills(KoboldSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = [self.hot_breath, self.bite, self.slash, self.fireball, self.flamethrower, self.talon_drop]

    def fireball(self, caster, target, cost=10, base_pow=6, accuracy=70):
        print(f"{caster.name} hurls a plume of fire at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)

    def flamethrower(self, caster, target, cost=20, base_pow=10, accuracy=80):
        print(f"{caster.name} sends all consuming flame at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)

    def talon_drop(self, caster, target, cost=10, base_pow=5, accuracy=100):
        print(f"{caster.name} dives at {target.name} with their talons!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
