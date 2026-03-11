from stats import Stats

class Race():
    def __init__(self):
        self.race_name = ""
    
    def trait(self):
        pass


class PlayerRace(Race):
    def __init__(self):
        super().__init__()
        stat_bonuses = Stats()


class Human(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "human"
        stat_bonuses = Stats()

    def trait(self):
        pass
  

class Dwarf(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "dwarf"
        stat_bonuses = Stats() 

    def trait(self):
        pass


class Elf(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "elf"
        stat_bonuses = Stats() 

    def trait(self):
        pass


class Goliath(PlayerRace):
    def __init__(self):
        super().__init__()
        self.race_name = "goliath"
        stat_bonuses = Stats() 
        
    def trait(self):
        pass
