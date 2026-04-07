from loot.item_libs.armors import *
from loot.item_libs.weapons import *
from loot.make_loot import LootMaker
from systems.units.units_base import Monster, Player
from systems.units.monster_races import *
from systems.units.player_races import *
from systems.units.classes import *
from dungeon.dgn_gen import Dungeon


def test_armors():
    armor1 = HeavyHead("busted bronze")
    armor2 = LootMaker().generate_armor(50)
    print(armor1.name)
    print(armor2.name)
    if armor1.name == armor2.name:
        print(True)
    else:
        print(False)

def test_weapons():
    weapon1 = Sword("busted bronze")
    weapon2 = LootMaker().generate_weapon(50)
    print(weapon1.name)
    print(weapon2.name)
    if weapon1.name == weapon2.name:
        print(True)
    else:
        print(False)

def loot_drop():
    monster_race = "Slime"
    monster = Monster(monster_race)
    monster.add_loot_equipment(1)
    player = Player("seb", Human(), Warrior(), 1)
    dungeon = Dungeon(player)
    while True:
        dungeon.start_combat(player, monster)
        

loot_drop()