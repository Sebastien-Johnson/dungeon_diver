from ..items_base import HeadPiece, ChestPiece, ArmPiece, LegPiece
from systems.stats import Stats

class LightHead(HeadPiece):
    def __init__(self, quality, name="Hat", item_type="head"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,0,1,0,0,1,0)
        self.med_qual = Stats(0,2,0,3,0,0,3,0)
        self.high_qual = Stats(0,3,0,5,0,0,5,0)
        self.stats = self.choose_linen_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)
        
class MediumHead(HeadPiece):
    def __init__(self, quality, name="Hood", item_type="head"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,1,1,1,0,0,0)
        self.med_qual = Stats(0,0,2,3,3,0,0,0)
        self.high_qual = Stats(0,0,3,5,5,0,0,0)
        self.stats = self.choose_leather_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class HeavyHead(HeadPiece):
    def __init__(self, quality, name="Helm", item_type="head"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(2,2,2,-1,0,0,0,0)
        self.med_qual = Stats(4,4,4,-3,0,0,0,0)
        self.high_qual = Stats(6,6,6,-5,0,0,0,0)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class LightChest(ChestPiece):
    def __init__(self, quality, name="Robe", item_type="chest"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,0,1,0,0,1,0)
        self.med_qual = Stats(0,2,0,3,0,0,3,0)
        self.high_qual = Stats(0,3,0,5,0,0,5,0)
        self.stats = self.choose_linen_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class MediumChest(ChestPiece):
    def __init__(self, quality, name="Vest", item_type="chest"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,1,1,1,0,0,0)
        self.med_qual = Stats(0,0,2,3,3,0,0,0)
        self.high_qual = Stats(0,0,3,5,5,0,0,0)
        self.stats = self.choose_leather_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class HeavyChest(ChestPiece):
    def __init__(self, quality, name="Breastplate", item_type="chest"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(2,2,2,-1,0,0,0,0)
        self.med_qual = Stats(4,4,4,-3,0,0,0,0)
        self.high_qual = Stats(6,6,6,-5,0,0,0,0)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class LightArms(ArmPiece):
    def __init__(self, quality, name="Gloves", item_type="arms"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,0,1,0,0,1,0)
        self.med_qual = Stats(0,2,0,3,0,0,3,0)
        self.high_qual = Stats(0,3,0,5,0,0,5,0) 
        self.stats = self.choose_linen_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class MediumArms(ArmPiece):
    def __init__(self, quality, name="Bracers", item_type="arms"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,1,1,1,0,0,0)
        self.med_qual = Stats(0,0,2,3,3,0,0,0)
        self.high_qual = Stats(0,0,3,5,5,0,0,0)
        self.stats = self.choose_leather_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class HeavyArms(ArmPiece):
    def __init__(self, quality, name="Gauntlets", item_type="arms"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(2,2,2,-1,0,0,0,0)
        self.med_qual = Stats(4,4,4,-3,0,0,0,0)
        self.high_qual = Stats(6,6,6,-5,0,0,0,0)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)


class LightLegs(LegPiece):
    def __init__(self, quality, name="Slippers", item_type="legs"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,1,0,1,0,0,1,0)
        self.med_qual = Stats(0,2,0,3,0,0,3,0)
        self.high_qual = Stats(0,3,0,5,0,0,5,0)
        self.stats = self.choose_linen_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class MediumLegs(LegPiece):
    def __init__(self, quality, name="Boots", item_type="legs"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(0,0,1,1,1,0,0,0)
        self.med_qual = Stats(0,0,2,3,3,0,0,0)
        self.high_qual = Stats(0,0,3,5,5,0,0,0)
        self.stats = self.choose_leather_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)

class HeavyLegs(LegPiece):
    def __init__(self, quality, name="Sabatons", item_type="legs"):
        super().__init__(quality, name, item_type)
        self.name = self.quality.title() + " " + name
        self.low_qual = Stats(2,2,2,-1,0,0,0,0)
        self.med_qual = Stats(4,4,4,-3,0,0,0,0)
        self.high_qual = Stats(6,6,6,-5,0,0,0,0)
        self.stats = self.choose_metal_quality(self.low_qual, self.med_qual, self.high_qual, self.quality)
        

