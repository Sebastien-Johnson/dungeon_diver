from ..stats import Stats
from ..skills.class_skills import *

class UnitClass():
    def __init__(self):
        self.classname = ""
        self.stats = Stats()
        

class Warrior(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "warrior"
        self.stats = Stats(3, 3, 2, 3, 0, 0, 30, 5)
        self.skills = WarriorSkills()

class Ranger(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "ranger"
        self.stats = Stats(2, 2, 2, 5, 0, 0, 30, 4)
        self.skills = RangerSkills()

class Mage(UnitClass): 
    def __init__(self):
        super().__init__()
        self.classname = "mage"
        self.stats = Stats(2, 2, 2, 2, 40, 5, 0, 0)
        self.skills = MageSkills()

class Cleric(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "cleric"
        self.stats = Stats(5, 2, 2, 2, 35, 0, 0, 3)
        self.skills = ClericSkills()

class Lesser(UnitClass):
    def __init__(self):
        super().__init__()
        self.name = "lesser"
        self.bonus_stats = Stats(1, 1, 1, 1, 10, 1, 10, 1)

class Greater(UnitClass):
    def __init__(self):
        super().__init__()
        self.name = "greater"
        self.bonus_stats = Stats(2, 2, 2, 2, 20, 2, 20, 2)

class High(UnitClass):
    def __init__(self):
        super().__init__()
        self.name = "high"
        self.bonus_stats = Stats(3, 3, 3, 3, 30, 3, 30, 3)