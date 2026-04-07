from ..items_base import Weapon
from systems.stats import Stats

class Shield(Weapon):
    def __init__(self, quality, name="Shield", hands=1):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,1,0,0,0,0,0)
        self.med_qual = Stats(0,3,3,0,0,0,0,0)
        self.high_qual = Stats(0,5,5,0,0,0,0,0)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)


class Dagger(Weapon):
    def __init__(self, quality, name="Dagger", hands=1):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,0,1,0,0,0,1)
        self.med_qual = Stats(0,0,0,3,0,0,0,3)
        self.high_qual = Stats(0,0,0,3,0,0,0,3)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)
        

class Sword(Weapon):
    def __init__(self, quality, name="Sword", hands=2):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,0,-1,0,0,0,3)
        self.med_qual = Stats(0,0,0,-2,0,0,0,6)
        self.high_qual = Stats(0,0,0,-3,0,0,0,9)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class TwoHander(Weapon):
    def __init__(self, quality, name="Two hander", hands=2):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,1,-1,0,0,0,5)
        self.med_qual = Stats(0,2,2,-3,0,0,0,10)
        self.high_qual = Stats(0,3,3,-5,0,0,0,15)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class Wand(Weapon):
    def __init__(self, quality, name="Wand", hands=1):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,0,1,0,3,0,0)
        self.med_qual = Stats(0,0,0,3,0,6,0,0)
        self.high_qual = Stats(0,0,0,5,0,9,0,0)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class Orb(Weapon):
    def __init__(self, quality, name="Orb", hands=1):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,1,0,5,1,0,0)
        self.med_qual = Stats(0,0,2,0,10,2,0,0)
        self.high_qual = Stats(0,0,3,0,15,3,0,0)
        self.stats = self.choose_orb_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)


class Staff(Weapon):
    def __init__(self, quality, name="Staff", hands=2):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,1,0,0,5,0,0)
        self.med_qual = Stats(0,1,1,0,0,10,0,0)
        self.high_qual = Stats(0,1,1,0,0,15,0,0)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class Bow(Weapon):
    def __init__(self, quality, name="Bow", hands=2):
        super().__init__(quality, name, hands)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,0,2,0,0,0,5)
        self.med_qual = Stats(0,0,0,4,0,0,0,10)
        self.high_qual = Stats(0,10,0,6,0,0,0,15)
        self.stats = self.choose_wood_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)