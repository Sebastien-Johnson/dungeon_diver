import time, sys
from systems.units.units_base import *
from systems.units.classes import *
from systems.units.player_races import *
from .dgn_gen import *


class Game():
    def __init__(self):
        pass

    def game_start(self):
        time.sleep(1)
        self.type_text(f"Welcome,.. to the dungeon.\n")
        time.sleep(1)
        player1 = self.create_adventurer()
        print("==============================================")
        self.type_text(f"Hello {player1.name} the {player1.race.race_name} {player1.unit_class.classname}!")
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
        self.type_text("What's your name adventurer?")
        name = input().capitalize()
        self.type_text("")
        return name

    def check_race(self):
        valid_races = ["human", "dwarf", "elf", "goliath"]
        self.type_text("What race are you?")
        self.type_text("[Human, Dwarf, Elf, Goliath]")
        player_race = input().lower()
        self.type_text("")

        while True:
            if player_race in valid_races:
                return player_race
            else:
                self.type_text(f"Sorry, '{player_race}' is not a known race. Try again.")
                player_race = input().lower()

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
            case _:
                return ValueError("no race")
    
    def check_class(self):
        valid_classes = ["warrior", "mage", "cleric", "ranger"]
        self.type_text("What class are you?")
        self.type_text("[Warrior, Mage, Cleric, Ranger]")
        player_class = input().lower()
        self.type_text("")

        while True:
            if player_class in valid_classes:
                return player_class
            else:
                self.type_text(f"Sorry, '{player_class}' is not a known race. Try again.")
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
            case _:
                return ValueError("unemployed")

    def start_dungeon(self, player):
        new_dungeon = Dungeon(player)
        new_dungeon.generate_dungeon()
        self.check_if_replay()

    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")