import random
from .combat import Combat
from systems.monster_races import *

class Dungeon():
    def __init__(self, player):
        self.dng_lvl_count = 1
        self.player = player
        self.lower_monsters = [Slime(), Bat(), Goblin()]
        self.middle_monsters = [Kobold(), DireWolf(), Troll()]
        self.higher_monsters = [Giant(), Dragon()]
        self.monster = self.generate_monster(self.dng_lvl_count)
        self.curent_lvl = DungeonLvl(self.player, self.monster)
        

    def generate_dng_lvl(self):
        self.dng_lvl_count += 1
        #allow for potions between levels
        if self.dng_lvl_count%10 == 0:
            pass
            #check if current lvl is rest area
        else:
            self.curent_lvl = DungeonLvl(self.player, self.monster)
            self.generate_dng_lvl()
        

    def generate_monster(self, dng_lvl_count):
        if dng_lvl_count%10 in range(1, 4) or dng_lvl_count in range(1, 4):
            return random.choice(self.lower_monsters)
        elif dng_lvl_count%10 in range(4, 7) or dng_lvl_count in range(4, 7):
            return random.choice(self.middle_monsters)
        elif dng_lvl_count%10 in range(7, 10) or dng_lvl_count in range(7, 10):
            return random.choice(self.higher_monsters)
        #use dungeon level for stat scaling

class DungeonLvl():
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster 

    def start_combat(self, player, monster):
        dng_lvl_combat = Combat(player, monster)
        while player.stats.current_health > 0 and monster.stats.current_health > 0:
            dng_lvl_combat.combat_instance(player, monster)

    