import random
from .combat import Combat
from systems.monster_races import *
from systems.units import Monster

class Dungeon():
    def __init__(self, player):
        self.dng_lvl_count = 0
        self.player = player
        self.lower_monsters = [Slime(), Bat(), Goblin()]
        self.middle_monsters = [Kobold(), DireWolf(), Troll()]
        self.higher_monsters = [Giant(), Dragon()]
        
        

    def generate_dng_lvl(self):
        self.dng_lvl_count += 1
        #allow for potions between levels
        if self.dng_lvl_count%10 == 0:
            pass
            #check if current lvl is rest area
        else:
            monster = self.generate_monster(self.dng_lvl_count)
            print(f"You descend to floor {self.dng_lvl_count} of the dungeon...\n")
            print(f"A {monster.name} approaches!!\n")
            self.start_combat(self.player, monster)
            self.generate_dng_lvl()
        

    def generate_monster(self, dng_lvl_count):
        if dng_lvl_count%10 in range(1, 4) or dng_lvl_count in range(1, 4):
            monster_race = random.choice(self.lower_monsters)
            return Monster(monster_race)
        elif dng_lvl_count%10 in range(4, 7) or dng_lvl_count in range(4, 7):
            monster_race = random.choice(self.middle_monsters)
            return Monster(monster_race)
        elif dng_lvl_count%10 in range(7, 10) or dng_lvl_count in range(7, 10):
            monster_race = random.choice(self.higher_monsters)
            return Monster(monster_race)
        #use dungeon level for stat scaling
        #add random selection for monster "class", larger choice range for deep dungeon levels

    def start_combat(self, player, monster):
        dng_lvl_combat = Combat(player, monster)
        while player.base_stats.current_health > 0 and monster.base_stats.current_health > 0:
            dng_lvl_combat.combat_instance(player, monster)
        print(f"Level {self.dng_lvl_count} complete!\n")

    