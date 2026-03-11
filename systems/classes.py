from stats import Stats

class UnitClass():
    def __init__(self):
        self.classname = ""
        self.stats = Stats()
        self.abilities = {}

class Warrior(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "warrior"
        self.stats = Stats(4, 4, 2, 3, None, None, 30, 3)

class Ranger(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "ranger"
        self.stats = Stats(2, 2, 2, 5, None, None, 30, 5)

class Mage(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "mage"
        self.stats = Stats(2, 2, 2, 1, 30, 9, None, None)

class Cleric(UnitClass):
    def __init__(self):
        super().__init__()
        self.classname = "cleric"
        self.stats = Stats(2, 2, 2, 5, None, None, 30, 5)