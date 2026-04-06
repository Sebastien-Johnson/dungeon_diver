from ..stats import Stats

class Race():
    def __init__(self):
        self.race_name = ""
    
    def trait(self):
        pass


class PlayerRace(Race):
    def __init__(self):
        super().__init__()
        self.stat_bonuses = Stats()


class Human(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "human"
        self.stat_bonuses = Stats(1,1,1,1,0,0,0,0)

    def trait(self):
        pass
  

class Dwarf(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "dwarf"
        self.stat_bonuses = Stats(3,1,0,0,0,0,10,0) 

    def trait(self):
        pass


class Elf(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "elf"
        self.stat_bonuses = Stats(0,0,1,1,10,2,0,0) 

    def trait(self):
        pass


class Goliath(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "goliath"
        self.stat_bonuses = Stats(0,1,1,0,0,0,0,3) 
        
    def trait(self):
        pass
