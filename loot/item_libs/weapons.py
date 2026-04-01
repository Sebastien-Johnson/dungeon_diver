from items_base import Weapon
from systems.stats import Stats

class Shield(Weapon):
    def __init__(self, name, quality, item_type="shield", hands=1):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "musty birch":
                self.stats = Stats(0,1,1,0,0,0,0,0)
            case "ok oak":
                self.stats = Stats(0,3,3,0,0,0,0,0)
            case "fine pine":
                self.stats = Stats(0,5,5,0,0,0,0,0)


class Dagger(Weapon):
    def __init__(self, name, quality, item_type="dagger", hands=1):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "bronze":
                self.stats = Stats(0,0,0,1,0,0,0,1)
            case "iron":
                self.stats = Stats(0,0,0,3,0,0,0,3)
            case "steel":
                self.stats = Stats(0,0,0,5,0,0,0,5)


class Sword(Weapon):
    def __init__(self, name, quality, item_type="sword", hands=2):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "bronze":
                self.stats = Stats(0,0,0,-1,0,0,0,3)
            case "iron":
                self.stats = Stats(0,0,0,-2,0,0,0,6)
            case "steel":
                self.stats = Stats(0,0,0,-3,0,0,0,9)

class TwoHander(Weapon):
    def __init__(self, name, quality, item_type="two hander", hands=2):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "bronze":
                self.stats = Stats(0,1,1,-1,0,0,0,5)
            case "iron":
                self.stats = Stats(0,2,2,-3,0,0,0,10)
            case "steel":
                self.stats = Stats(0,3,3,-5,0,0,0,15)

class Wand(Weapon):
    def __init__(self, name, quality, item_type="wand", hands=1):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "musty birch":
                self.stats = Stats(0,0,0,1,0,3,0,0)
            case "ok oak":
                self.stats = Stats(0,0,0,3,0,6,0,0)
            case "fine pine":
                self.stats = Stats(0,0,0,5,0,9,0,0)

class Orb(Weapon):
    def __init__(self, name, quality, item_type="orb", hands=1):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "cloudy":
                self.stats = Stats(0,0,1,0,5,1,0,0)
            case "clear":
                self.stats = Stats(0,0,2,0,10,2,0,0)
            case "flourescent":
                self.stats = Stats(0,0,3,0,15,3,0,0)


class Staff(Weapon):
    def __init__(self, name, quality, item_type="magic staff", hands=2):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "musty birch":
                self.stats = Stats(0,1,1,0,0,5,0,0)
            case "ok oak":
                self.stats = Stats(0,1,1,0,0,10,0,0)
            case "fine pine":
                self.stats = Stats(0,1,1,0,0,15,0,0)

class Bow(Weapon):
    def __init__(self, name, quality, item_type, hands):
        super().__init__(name, quality, item_type, hands)
        match quality:
            case "musty birch":
                self.stats = Stats(0,0,0,2,0,0,0,5)
            case "ok oak":
                self.stats = Stats(0,0,0,4,0,0,0,10)
            case "fine pine":
                self.stats = Stats(0,10,0,6,0,0,0,15)