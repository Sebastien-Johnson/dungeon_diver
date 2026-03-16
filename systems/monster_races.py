from player_races import Race
from skills.monster_skills import *
from stats import Stats


class MonsterRace(Race):
    def __init__(self):
        super().__init__()
        self.base_stats = Stats()

    def trait(self):
        pass

class Slime(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "slime"
        self.base_stats = Stats()
        self.skills = SlimeSkills()

    def trait(self):
        pass

class Bat(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "bat"
        self.base_stats = Stats()
        self.skills = BatSkills()

    def trait(self):
        pass

class Goblin(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "goblin"
        self.base_stats = Stats()
        self.skills = GoblinSkills()

    def trait(self):
        pass

class Kobold(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "kobold"
        self.base_stats = Stats()
        self.skills = KoboldSkills()

    def trait(self):
        pass

class DireWolf(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "dire wolf"
        self.base_stats = Stats()
        self.skills = DirewolfSkills()

    def trait(self):
        pass

class Troll(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "troll"
        self.base_stats = Stats()
        self.skills = TrollSkills()

    def trait(self):
        pass

class Giant(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "giant"
        self.base_stats = Stats()
        self.skills = GiantSkills()

    def trait(self):
        pass

class Dragon(MonsterRace):
    def __init__(self):
        super().__init__()
        self.race_name = "dragon"
        self.base_stats = Stats()
        self.skills = DragonSkills()

    def trait(self):
        pass