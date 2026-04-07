from loot.item_libs.armors import *
from loot.item_libs.weapons import *
from loot.make_loot import LootMaker

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


test_weapons()