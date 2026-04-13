from .skill_base import PhysSkills, MagSkills

class SlimeSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()
    
        self.skill_list = ["absorb"]
    
    def absorb(self, caster, target, cost=5, base_pow=0, accuracy=75):
        self.type_text(f"{caster.name} learches at {target.name} to leach their essence!")
        if self.phys_attack(caster, target, cost, base_pow=0, accuracy=accuracy):
            self.phys_drain(caster, caster, cost, base_pow, 100)
        self.monster_status(caster, target)

class BatSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = ["scratch", "vamp_bite"]

    def scratch(self, caster, target, cost=5, base_pow=1, accuracy=85):
        self.type_text(f"{caster.name} scratches {target.name} with their claws!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

    def vamp_bite(self, caster, target, cost=5, base_pow=0, accuracy=75):
        self.type_text(f"{caster.name} learches at {target.name} to leach their essence!") 
        if self.phys_attack(caster, target, cost, base_pow=0, accuracy=accuracy):
            self.phys_drain(caster, caster, cost, base_pow, 100)
        self.monster_status(caster, target)

class GoblinSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = ["stab", "sling"]

    def stab(self, caster, target, cost=5, base_pow=1, accuracy=95):
        self.type_text(f"{caster.name} stabs at {target.name}!") 
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

    def sling(self, caster, target, cost=5, base_pow=2, accuracy=80):
        self.type_text(f"{caster.name} slings a rock at {target.name}!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)
    

class DirewolfSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()
    
        self.skill_list = ["bite"]

    def bite(self, caster, target, cost=5, base_pow=3, accuracy=80):
        self.type_text(f"{caster.name} lunges to rend {target.name}'s flesh!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

class KoboldSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = ["hot_breath", "bite", "slash"]
    
    def hot_breath(self, caster, target, cost=5, base_pow=4, accuracy=60):
        self.type_text(f"{caster.name} sends a wave of fire at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

    def bite(self, caster, target, cost=5, base_pow=4, accuracy=80):
        self.type_text(f"{caster.name} lunges to rend {target.name}'s flesh!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)
    
    def slash(self, caster, target, cost=5, base_pow=1, accuracy=95):
        self.type_text(f"{caster.name} slashes at {target.name} with their {caster.inventory.weapon}!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

class TrollSkills(PhysSkills, MagSkills):
    def __init__(self):
        super().__init__()
    
        self.skill_list = ["skull_splitter"]

    def skull_splitter(self, caster, target, cost=8, base_pow=6, accuracy=60):
        self.type_text(f"{caster.name} drops their {caster.inventory.weapons} down at {target.name}'s head with all their might!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

class GiantSkills(TrollSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = ["skull_splitter", "boulder_drop", "earthquake"]

    def boulder_drop(self, caster, target, cost=20, base_pow=10, accuracy=80):
        self.type_text(f"{caster.name} RKO's a boulder over {target.name}'s head!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

    def earthquake(self, caster, target, cost=30, base_pow=10, accuracy=100):
        self.type_text(f"{caster.name} splits the earth beneath {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

class DragonSkills(KoboldSkills):
    def __init__(self):
        super().__init__()

        self.skill_list = ["hot_breath", "bite", "slash", "fireball", "flamethrower", "talon_drop"]

    def fireball(self, caster, target, cost=10, base_pow=6, accuracy=70):
        self.type_text(f"{caster.name} hurls a plume of fire at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

    def flamethrower(self, caster, target, cost=20, base_pow=10, accuracy=80):
        self.type_text(f"{caster.name} sends all consuming flame at {target.name}!")
        self.mag_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)

    def talon_drop(self, caster, target, cost=10, base_pow=5, accuracy=100):
        self.type_text(f"{caster.name} dives at {target.name} with their talons!")
        self.phys_attack(caster, target, cost, base_pow, accuracy)
        self.monster_status(caster, target)