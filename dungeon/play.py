from systems.units import *
from systems.classes import *
from systems.player_races import *
from .dgn_gen import *

class Game():
    def __init__(self):
        pass

    def game_start(self):
        print("Welcome,.. to the dungeon.\n")
        player1 = self.create_adventurer()
        self.start_dungeon(player1)

    def create_adventurer(self):
        name = self.get_name()
        race = self.race_to_obj(self.check_race())
        player_class = self.player_class_to_obj(self.check_class())
        return Player(name, race, player_class)
    
    def get_name(self):
        print("What's your name adventurer?\n")
        name = input()
        print("\n")
        return name

    def check_race(self):
        valid_races = ["human", "dwarf", "elf", "goliath"]
        known_race = False
        print("What race are you?\n")
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
        print(["Warrior, Mage, Cleric, Ranger\n"])
        player_class = input().lower()
        print("\n")

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

    def start_dungeon(self, player):
        new_dungeon = Dungeon(player)
        new_dungeon.generate_dng_lvl()