import random, time, sys
from systems.units.monster_races import *
from .combat import Combat
from systems.units.units_base import Monster
from systems.units.classes import Lesser, Greater, High


class Dungeon():
    def __init__(self, player):
        self.curr_dng_lvl = 0
        self.player = player
        self.lower_monsters = ["Slime", "Bat", "Goblin"]
        self.middle_monsters = ["Kobold", "Direwolf", "Troll"]
        self.higher_monsters = ["Giant", "Dragon"]
        

    def generate_dungeon(self):
        self.curr_dng_lvl += 1
        while self.player.base_stats.current_health > 0:
            monster = self.generate_monster(self.curr_dng_lvl)
            self.type_text("")
            self.type_text(f"You descend to floor {self.curr_dng_lvl} of the dungeon...")
            time.sleep(1)
            self.type_text(f"A {monster.name} approaches!!\n")
            time.sleep(1)
            self.start_combat(self.player, monster)
            self.curr_dng_lvl += 1
        

    def generate_monster(self, curr_dng_lvl):
        if curr_dng_lvl == 101:
            self.type_text(f"\x1B[3m(A deep, Keith David sounding voice booms in)\x1B[0m")
            self.type_text(f"'CONGRATULATIONS, little mouse, on clearing those pests from my doorstep...'")
            self.type_text(f"'I really hate when my pets try to eat those vermin.'")
            self.type_text(f"'\x1B[3mYou should yourself out, before they see themselves to you\x1B[0m'")
            sys.exit()
        elif curr_dng_lvl%10 in range(1, 19) or curr_dng_lvl in range(1, 10):
            monster_race = self.spawn_rate()
            grade = self.monster_grade()
            monster = Monster(self.check_monster_race(monster_race), grade)
            monster.add_loot_equipment(self.curr_dng_lvl)
            monster.base_stats.lvl_up_to_lvl(monster.initial_stats, self.player.current_lvl)
            monster.scale_xp(self.player.current_lvl)
            return monster
        elif curr_dng_lvl%10 == 0:
            self.type_text("There appears to be no monsters around...")
            self.type_text("You've finally reach a rest area!")
            self.type_text(f"{self.player.name} rested and their stats were restored!!")
            self.player.long_rest()

    def spawn_rate(self):
        rate = random.randrange(100)
        med_rate = 10 + (self.curr_dng_lvl*.75)
        high_rate = self.curr_dng_lvl *.25
        if rate <= high_rate:
            return random.choice(self.higher_monsters)
        elif rate <= med_rate:
            return random.choice(self.middle_monsters)
        else:
            return random.choice(self.lower_monsters)

    def monster_grade(self):
        rate = random.randrange(100)
        med_rate = 40
        high_rate = 20
        if rate <= high_rate:
            return High()
        elif rate <= med_rate:
            return Greater()
        else:
            return Lesser()

    def check_monster_race(self, monster_race):
        match monster_race:
            case "Slime":
                return Slime()
            case "Bat":
                return Bat()
            case "Goblin":
                return Goblin()
            case "Kobold":
                return Kobold()
            case "Direwolf":
                return DireWolf()
            case "Troll":
                return Troll()
            case "Giant":
                return Giant()
            case "Dragon":
                return Dragon()
            

    def start_combat(self, player, monster):
        dng_lvl_combat = Combat(player, monster)
        self.type_text(f"{player.name} health: {player.base_stats.current_health}/{player.base_stats.max_health}.")
        self.type_text(f"{monster.name} health: {monster.base_stats.current_health}/{monster.base_stats.max_health}.\n")
        time.sleep(1)
        while player.base_stats.current_health > 0 and monster.base_stats.current_health > 0:
            dng_lvl_combat.combat_instance(player, monster)
        self.type_text(f"Floor {self.curr_dng_lvl} complete!")
        monster.inventory.loot_body(player)
        self.cont(player)
        print("==============================================")
    

    def cont(self, player):
        self.type_text(f"Venture on? (y/n)")
        reply = input().lower()
        while True:
            if reply in ["yes", "y"]:
                self.type_text(f"{player.name} catches their breath between floors.")
                player.short_rest(self.curr_dng_lvl)
                break
            elif reply in ["n", "no"]:
                self.type_text("Sorry, didn't hear you (coward).")
                reply = input().lower()
                if reply in ["yes", "y"]:
                    continue
                elif reply in ["n", "no"]:
                    self.type_text("This is why no one will remember your name")
                    sys.exit()
            else:
                self.type_text("Unclear input, try again.")
                reply = input().lower()
            


    def rest_menu(self):
        while True:
            self.type_text("Menu (select number):")
            self.type_text("1. Current stats\n2. Change equipment\n3. Move on")
            reply = input().lower()
            if reply == "1":
                self.player.base_stats.show_stat_update()
                i = 0
                self.type_text("Equipped items:")
                for item in self.player.inventory.equipped:
                    self.type_text(f"{i+1}. {item.name} ({item.item_type})")
                    item.stats.show_item_stats()
                    i += 1
            elif reply == "2":
                self.player.inventory.change_equipment()
            elif reply == "3":
                self.cont(self.player)
                break
            else:
                self.type_text("Unclear input, try again.")
                reply = input().lower()


    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")

    