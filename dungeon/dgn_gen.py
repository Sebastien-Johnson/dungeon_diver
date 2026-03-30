import random, time
from .combat import Combat
from systems.monster_races import *
from systems.units import Monster

class Dungeon():
    def __init__(self, player):
        self.dng_lvl_count = 0
        self.player = player
        self.lower_monsters = ["slime", "bat", "goblin"]
        self.middle_monsters = ["kobold", "direwolf", "troll"]
        self.higher_monsters = ["giant", "dragon"]
        
        

    def generate_dungeon(self):
        self.dng_lvl_count += 1
        #allow for potions between levels
        if self.dng_lvl_count%10 == 0:
            pass
            #check if current lvl is rest area
        else:
            while self.player.base_stats.current_health > 0:
                monster = self.generate_monster(self.dng_lvl_count)
                print(f"You descend to floor {self.dng_lvl_count} of the dungeon...\n")
                time.sleep(1)
                print(f"A {monster.name} approaches!!\n")
                time.sleep(1)
                self.start_combat(self.player, monster)
                self.dng_lvl_count += 1
        

    def generate_monster(self, dng_lvl_count):
        if dng_lvl_count%10 in range(1, 4) or dng_lvl_count in range(1, 4):
            monster_race = random.choice(self.lower_monsters)
            return Monster(self.check_monster_race(monster_race))
        elif dng_lvl_count%10 in range(4, 7) or dng_lvl_count in range(4, 7):
            monster_race = random.choice(self.middle_monsters)
            return Monster(self.check_monster_race(monster_race))
        elif dng_lvl_count%10 in range(7, 10) or dng_lvl_count in range(7, 10):
            monster_race = random.choice(self.higher_monsters)
            return Monster(self.check_monster_race(monster_race))
        #use dungeon level for stat scaling
        #add random selection for monster "class", larger choice range for deep dungeon levels

    def check_monster_race(self, monster_race):
        match monster_race:
            case "slime":
                return Slime()
            case "bat":
                return Bat()
            case "goblin":
                return Goblin()
            case "kobold":
                return Kobold()
            case "direwolf":
                return DireWolf()
            case "troll":
                return Troll()
            case "giant":
                return Giant()
            case "dragon":
                return Dragon()
            

    def start_combat(self, player, monster):
        dng_lvl_combat = Combat(player, monster)
        print(f"{player.name} health: {player.base_stats.current_health}/{player.base_stats.max_health}")
        print(f"{monster.name} health: {monster.base_stats.current_health}/{monster.base_stats.max_health}\n")
        time.sleep(1)
        while player.base_stats.current_health > 0 and monster.base_stats.current_health > 0:
            dng_lvl_combat.combat_instance(player, monster)
        print(f"Level {self.dng_lvl_count} complete!\n")
        self.cont()
        print("==============================================")

    def cont(self):
        print(f"Venture on? (y/n)")
        reply = input().lower()
        while True:
            if reply in ["yes", "y"]:
                break
            else:
                print("Sorry, didn't hear you (coward).")
                reply = input().lower()

    