from systems.stats import Stats
class LootMaker():
    def __init__(self):
        self.wood_weapons = ["dagger", "sword", "two hander"]
        self.metal_weapons = ["shield", "wand", "staff", "bow"]
        self.wood_qualities = ["musty birch", "ok oak", "fine pine"]
        self.metal_qualities = ["busted bronze", "aight iron", "sick steel"]
        self.orb_qualities = ["cloudy", "clear", "flourescent"]
        self.fabric_qualities = []
        self.leather_qualities = []
        self.dagger_qualities = {"busted bronze": Stats(0,0,0,1,0,0,0,1), "aight iron" : Stats(0,0,0,3,0,0,0,3), "sick steel" : Stats(0,0,0,5,0,0,0,5)}


    

