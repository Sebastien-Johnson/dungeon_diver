from systems.units import *
from systems.classes import *
from systems.player_races import *
from .dgn_gen import *
import time

class Game():
    def __init__(self):
        pass

    def game_start(self):
        time.sleep(1)
        print("Welcome,.. to the dungeon.\n")
        time.sleep(1)
        player1 = self.create_adventurer()
        print("==============================================")
        print(f"Hello {player1.name} the {player1.race.race_name} {player1.unit_class.classname}!")
        print("==============================================\n")
        time.sleep(1)
        self.start_dungeon(player1)

    def create_adventurer(self):
        name = self.get_name()
        time.sleep(1)
        race = self.race_to_obj(self.check_race())
        time.sleep(1)
        player_class = self.player_class_to_obj(self.check_class())
        time.sleep(1)
        return Player(name, race, player_class)
    
    def get_name(self):
        print("What's your name adventurer?\n")
        name = input().capitalize()
        print("\n")
        return name

    def check_race(self):
        valid_races = ["human", "dwarf", "elf", "goliath"]
        known_race = False
        print("What race are you?")
        print("[Human, Dwarf, Elf, Goliath]\n")
        player_race = input().lower()
        print("\n")

        while known_race == False:
            if player_race.lower() in valid_races:
                known_race = True
                return player_race
            else:
                print(f"Sorry, '{player_race}' is not a known race. Try again.\n")
                player_race = input()

    def race_to_obj(self, race):
        match race:
            case "human":
                return Human() 
            case "elf":
                return Elf()
            case "dwarf":
                return Dwarf()
            case "goliath":
                return Goliath()
    
    def check_class(self):
        valid_classes = ["warrior", "mage", "cleric", "ranger"]
        propper_class = False
        print("What class are you?")
        print("[Warrior, Mage, Cleric, Ranger]\n")
        player_class = input().lower()
        

        while propper_class == False:
            if player_class.lower() in valid_classes:
                propper_class = True
                return player_class
            else:
                print(f"Sorry, '{player_class}' is not a propper class. Try again.\n")
                player_class = input().lower()
    
    def player_class_to_obj(self, player_class):
        match player_class:
            case "warrior":
                return Warrior()
            case "ranger":
                return Ranger()
            case "mage":
                return Mage()
            case "cleric":
                return Cleric()
            
    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}")

    def start_dungeon(self, player):
        new_dungeon = Dungeon(player)
        new_dungeon.generate_dungeon()