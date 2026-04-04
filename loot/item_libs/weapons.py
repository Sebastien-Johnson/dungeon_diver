from items_base import Weapon
from systems.stats import Stats

class Shield(Weapon):
    def __init__(self, name, quality, item_type="shield", hands=1):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,1,1,0,0,0,0,0)
        self.med_qual = Stats(0,3,3,0,0,0,0,0)
        self.high_qual = Stats(0,5,5,0,0,0,0,0)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)


class Dagger(Weapon):
    def __init__(self, name, quality, item_type="dagger", hands=1):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,0,0,1,0,0,0,1)
        self.med_qual = Stats(0,0,0,3,0,0,0,3)
        self.high_qual = Stats(0,0,0,3,0,0,0,3)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)
        


class Sword(Weapon):
    def __init__(self, name, quality, item_type="sword", hands=2):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,0,0,-1,0,0,0,3)
        self.med_qual = Stats(0,0,0,-2,0,0,0,6)
        self.high_qual = Stats(0,0,0,-3,0,0,0,9)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class TwoHander(Weapon):
    def __init__(self, name, quality, item_type="two hander", hands=2):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,1,1,-1,0,0,0,5)
        self.med_qual = Stats(0,2,2,-3,0,0,0,10)
        self.high_qual = Stats(0,3,3,-5,0,0,0,15)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class Wand(Weapon):
    def __init__(self, name, quality, item_type="wand", hands=1):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,0,0,1,0,3,0,0)
        self.med_qual = Stats(0,0,0,3,0,6,0,0)
        self.high_qual = Stats(0,0,0,5,0,9,0,0)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class Orb(Weapon):
    def __init__(self, name, quality, item_type="orb", hands=1):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,0,1,0,5,1,0,0)
        self.med_qual = Stats(0,0,2,0,10,2,0,0)
        self.high_qual = Stats(0,0,3,0,15,3,0,0)
        self.stats = self.choose_orb_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)


class Staff(Weapon):
    def __init__(self, name, quality, item_type="magic staff", hands=2):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,1,1,0,0,5,0,0)
        self.med_qual = Stats(0,1,1,0,0,10,0,0)
        self.high_qual = Stats(0,1,1,0,0,15,0,0)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class Bow(Weapon):
    def __init__(self, name, quality, item_type, hands):
        super().__init__(name, quality, item_type, hands)
        self.low_qual = Stats(0,0,0,2,0,0,0,5)
        self.med_qual = Stats(0,0,0,4,0,0,0,10)
        self.high_qual = Stats(0,10,0,6,0,0,0,15)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)