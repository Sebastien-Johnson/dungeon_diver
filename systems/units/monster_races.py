from .player_races import Race
from ..skills.monster_skills import *
from ..stats import Stats

class MonsterRace(Race):
    def __init__(self):
        super().__init__()
        self.base_stats = Stats()
        self.xp_val = int()

    def scale_xp(self, unit_lvl):
        xp_base = self.xp_val
        xp_multiplier = 1.25
        self.xp_val = xp_base*xp_multiplier*unit_lvl
    
class Slime(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Slime"
        self.base_stats = Stats(2, 0, 0, 1, 0, 0, 20, 3)
        self.skills = SlimeSkills()
        self.xp_val = 50


class Bat(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Bat"
        self.base_stats = Stats(2, 0, 0, 1, 0, 0, 20, 5)
        self.skills = BatSkills()
        self.xp_val = 50


class Goblin(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.base_stats = Stats(2, 0, 0, 1, 0, 0, 20, 5)
        self.skills = GoblinSkills()
        self.xp_val = 50


class Kobold(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Kobold"
        self.base_stats = Stats(1)
        self.skills = KoboldSkills()
        self.xp_val = 100


class DireWolf(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Dire wolf"
        self.base_stats = Stats(1)
        self.skills = DirewolfSkills()
        self.xp_val = 100


class Troll(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Troll"
        self.base_stats = Stats(1)
        self.skills = TrollSkills()
        self.xp_val = 100


class Giant(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Giant"
        self.base_stats = Stats(1)
        self.skills = GiantSkills()
        self.xp_val = 200


class Dragon(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "Dragon"
        self.base_stats = Stats(1)
        self.skills = DragonSkills(5, 0, 0, 1, 0, 0, 20, 5)
        self.xp_val = 400
