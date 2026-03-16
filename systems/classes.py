from stats import Stats
from systems.skills.class_skills import *

class UnitClass():
    def __init__(self):
        self.classname = ""
        self.stats = Stats()
        

class Warrior(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "warrior"
        self.stats = Stats(4, 4, 2, 3, None, None, 30, 3)
        self.skills = WarriorSkills()

class Ranger(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "ranger"
        self.stats = Stats(2, 2, 2, 5, None, None, 30, 5)
        self.skills = RangerSkills()

class Mage(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "mage"
        self.stats = Stats(2, 2, 2, 1, 30, 9, None, None)
        self.skills = MageSkills()

class Cleric(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "cleric"
        self.stats = Stats(2, 2, 2, 5, None, None, 30, 5)
        self.skills = ClericSkills()

class Low(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "low"
        self.stats = Stats(1, 1, 1, 1, 30, 1, 30, 1)

class Greater(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "greater"
        self.stats = Stats(2, 2, 2, 2, 40, 2, 40, 2)

class High(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "high"
        self.stats = Stats(3, 3, 3, 3, 50, 3, 50, 3)