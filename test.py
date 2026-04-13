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
        

def test_reequip():
    player1 = Player("seb", Human(), Warrior())

    weapon1 = Sword("busted bronze")
    helmet1 = HeavyHead("busted bronze")
    chest1 = HeavyChest("busted bronze")
    arms1 = HeavyArms("busted bronze")
    legs1 = HeavyLegs("busted bronze")
    to_equip = [weapon1, helmet1, chest1, arms1, legs1]

    for item in to_equip:
        player1.inventory.equip_item(item, player1)
    
    weapon2 = Dagger("busted bronze")
    helmet2 = LightHead("crusty cotton")
    chest2 = LightChest("crusty cotton")
    arms2 = LightArms("crusty cotton")
    legs2 = LightLegs("crusty cotton")
    to_bag = [weapon2, helmet2, chest2, arms2, legs2]

    for item in to_bag:
        player1.inventory.add_to_bag(item)

    
    player1.inventory.change_equipment(player1)

def type_text(text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")

type_text(f"\x1B[3m(A deep, Keith David sounding voice booms in)\x1B[0m")
type_text(f"'CONGRATULATIONS, little mouse, on clearing those pests from my doorstep!!'")
type_text(f"'I've yet to find a few minutes to do it myself and I really hate when my pets try to eat those vermin.'")
type_text(f"'That being said, you should see yourself out, before they see themselves to \x1B[3myou\x1B[0m...'")
