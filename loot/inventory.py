from .items_base import *
import time

class UnitInventory():
    def __init__(self):
        self.bag = []
        self.head = []
        self.chest = []
        self.legs = []
        self.arms = []
        self.weapons = []
        self.armors = []
        self.equipped = []

    def add_to_bag(self, item):
        self.bag.append(item)

    def take_from_bag(self, item):
        self.bag.remove(item)

    def throw_item(self, item):
        self.bag.remove(item)
    
    def equip_item(self, item, player):
        print("suiting up")
        if isinstance(item, Weapon):
            print("adding weapon")
            self.check_hands(player, item)
        elif isinstance(item, Equipment):
            print("adding armor")
            self.equip_armor(player, item)

    def equip_armor(self, player, new_armor):
        if self.armors:
            print("iterating armors")
            for armor in self.armors:
                if new_armor.item_type == armor.item_type:
                    player.total_stats.remove_stats(armor.stats)
                    player.total_stats.add_stats(new_armor.stats)
                    self.armors.remove(armor)
                    self.equipped.remove(armor)
                    self.add_to_bag(armor)  
                    match new_armor.item_type:
                        case "head":
                            self.head = new_armor
                        case "chest":
                            self.chest = new_armor
                        case "arms":
                            self.arms = new_armor
                        case "legs":
                            self.legs = new_armor
                        case _:
                            print("No matches")
        else:
             print("armors empty")
             print(new_armor.item_type)
             print(new_armor.stats)
             player.total_stats.add_stats(new_armor.stats)
             self.armors.append(armor)
             self.equipped.append(armor)
             match new_armor.item_type:
                case "head":
                    self.head = new_armor
                case "chest":
                    self.chest = new_armor
                case "arms":
                    self.arms = new_armor
                case "legs":
                    self.legs = new_armor
        print("Can't wear that there!")

    def equip_weapon(self, player, new_weapon):
        self.weapons.append(new_weapon)
        self.equipped.append(new_weapon)
        player.total_stats.add_stats(new_weapon.stats)

    def unequip_weapon(self, player, current_weapon):
        self.weapons.remove(current_weapon)
        self.add_to_bag(current_weapon)
        player.total_stats.remove_stats(current_weapon.stats)

        
    def check_hands(self, player, new_weapon):
        wpn_count = len(self.weapons)

        if wpn_count == 0:
            print("hands free, weapon equiped")
            self.equip_weapon(player, new_weapon)
            return
        
        if new_weapon.hands == 1:
            if wpn_count == 1:
                if self.weapons[0].hands == 1:
                    self.equip_weapon(player, new_weapon)
                    return
                else:
                    self.unequip_weapon(player, self.weapons[0])
                    self.equip_weapon(player, new_weapon)
                    return
                
            if wpn_count == 2: 
                for w in self.weapons:
                    print(f"Swap {new_weapon.name} for {w.name}? (y/n)")
                    x = input()
                    if x in ["yes", "y"]:
                        self.unequip_weapon(player, w)
                        self.equip_weapon(player, new_weapon)
                        break
                return
                

        if new_weapon.hands == 2:
            for w in self.weapons:
                self.unequip_weapon(player, w)
            self.equip_weapon(player, new_weapon)
            return
        print("did not equip weapon")

    def loot_body(self, player):
        print(self.armors)
        print(self.weapons)
        print(self.equipped)
        for i in self.equipped:
            self.type_text(f"They dropped a {i.name}!!")
            self.type_text("Take it? (y/n)")
            take = input()
            while True:
                if take in ["yes", "y"]:
                    self.type_text("Bag or equip? (1/2)")
                    bag_equip = input()
                    if bag_equip == "1":
                        player.inventory.add_to_bag(i, player)
                        break
                    elif bag_equip == "2":
                        player.inventory.equip_item(i, player)
                        break
                elif take in ["no", "n"]:
                    self.type_text("Oh well, your loss.")
                    break
                else:
                    self.type_text("Unclear answer, try again.")
                
    
    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")
