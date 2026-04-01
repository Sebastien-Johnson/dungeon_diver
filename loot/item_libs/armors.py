from items_base import HeadPiece, ChestPiece, ArmPiece, LegPiece
from systems.stats import Stats

class LightHead(HeadPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "cotton":
                self.stats = Stats(0,1,0,1,0,0,1,0)
            case "linen":
                self.stats = Stats(0,2,0,3,0,0,3,0)
            case "silk":
                self.stats = Stats(0,3,0,5,0,0,5,0)

class MediumHead(HeadPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "rawhide":
                self.stats = Stats(0,0,1,1,1,0,0,0)
            case "leather":
                self.stats = Stats(0,0,2,3,3,0,0,0)
            case "suede":
                self.stats = Stats(0,0,3,5,5,0,0,0)

class HeavyHead(HeadPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "bronze":
                self.stats = Stats(2,2,2,-1,0,0,0,0)
            case "steel":
                self.stats = Stats(4,4,4,-3,0,0,0,0)
            case "iron":
                self.stats = Stats(6,6,6,-5,0,0,0,0)

class LightChest(ChestPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "cotton":
                self.stats = Stats(0,1,0,1,0,0,1,0)
            case "linen":
                self.stats = Stats(0,2,0,3,0,0,3,0)
            case "silk":
                self.stats = Stats(0,3,0,5,0,0,5,0)

class MediumChest(ChestPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "rawhide":
                self.stats = Stats(0,0,1,1,1,0,0,0)
            case "leather":
                self.stats = Stats(0,0,2,3,3,0,0,0)
            case "suede":
                self.stats = Stats(0,0,3,5,5,0,0,0)

class HeavyChest(ChestPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "bronze":
                self.stats = Stats(2,2,2,-1,0,0,0,0)
            case "steel":
                self.stats = Stats(4,4,4,-3,0,0,0,0)
            case "iron":
                self.stats = Stats(6,6,6,-5,0,0,0,0)

class LightArms(ArmPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "cotton":
                self.stats = Stats(0,1,0,1,0,0,1,0)
            case "linen":
                self.stats = Stats(0,2,0,3,0,0,3,0)
            case "silk":
                self.stats = Stats(0,3,0,5,0,0,5,0)

class MediumArms(ArmPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "rawhide":
                self.stats = Stats(0,0,1,1,1,0,0,0)
            case "leather":
                self.stats = Stats(0,0,2,3,3,0,0,0)
            case "suede":
                self.stats = Stats(0,0,3,5,5,0,0,0)

class HeavyArms(ArmPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "bronze":
                self.stats = Stats(2,2,2,-1,0,0,0,0)
            case "steel":
                self.stats = Stats(4,4,4,-3,0,0,0,0)
            case "iron":
                self.stats = Stats(6,6,6,-5,0,0,0,0)


class LightLegs(LegPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "cotton":
                self.stats = Stats(0,1,0,1,0,0,1,0)
            case "linen":
                self.stats = Stats(0,2,0,3,0,0,3,0)
            case "silk":
                self.stats = Stats(0,3,0,5,0,0,5,0)

class MediumLegs(LegPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "rawhide":
                self.stats = Stats(0,0,1,1,1,0,0,0)
            case "leather":
                self.stats = Stats(0,0,2,3,3,0,0,0)
            case "suede":
                self.stats = Stats(0,0,3,5,5,0,0,0)

class HeavyLegs(LegPiece):
    def __init__(self, name, item_type, quality):
        super().__init__(name, item_type)
        self.quality = quality
        self.name = self.quality + name
        match self.quality:
            case "bronze":
                self.stats = Stats(2,2,2,-1,0,0,0,0)
            case "steel":
                self.stats = Stats(4,4,4,-3,0,0,0,0)
            case "iron":
                self.stats = Stats(6,6,6,-5,0,0,0,0)

        

