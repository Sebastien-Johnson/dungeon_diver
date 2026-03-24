from .player_races import Race
from .skills.monster_skills import *
from .stats import Stats


class MonsterRace(Race):
    def __init__(self):
        super().__init__()
        self.base_stats = Stats()

    def trait(self):
        pass

class Slime(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "slime"
        self.base_stats = Stats(1)
        self.skills = SlimeSkills()

    def trait(self):
        pass

class Bat(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "bat"
        self.base_stats = Stats(1)
        self.skills = BatSkills()

    def trait(self):
        pass

class Goblin(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "goblin"
        self.base_stats = Stats(1)
        self.skills = GoblinSkills()

    def trait(self):
        pass

class Kobold(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "kobold"
        self.base_stats = Stats(1)
        self.skills = KoboldSkills()

    def trait(self):
        pass

class DireWolf(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "dire wolf"
        self.base_stats = Stats(1)
        self.skills = DirewolfSkills()

    def trait(self):
        pass

class Troll(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "troll"
        self.base_stats = Stats(1)
        self.skills = TrollSkills()

    def trait(self):
        pass

class Giant(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "giant"
        self.base_stats = Stats(1)
        self.skills = GiantSkills()

    def trait(self):
        pass

class Dragon(MonsterRace):
    def __init__(self):
        super().__init__()
        self.name = "dragon"
        self.base_stats = Stats(1)
        self.skills = DragonSkills()

    def trait(self):
        pass