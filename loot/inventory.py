import time
from .items_base import *
from .item_libs.weapons import *


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
        self.type_text(f"{item.name} moved to bag.")

    def take_from_bag(self, item):
        self.bag.remove(item)

    def throw_item(self, item):
        self.bag.remove(item)
        self.type_text(f"{item.name} has been cast aside like a cart in the parking lot...")
    
    def equip_item(self, item, unit):
        if isinstance(item, Weapon):
            self.check_hands(unit, item)
        elif isinstance(item, Equipment):
            self.equip_armor(unit, item)

    def equip_armor(self, player, new_armor):
        if self.armors:
            for armor in self.armors:
                if new_armor.item_type == armor.item_type:
                    player.base_stats.remove_stats(armor.stats)
                    player.base_stats.add_stats(new_armor.stats)
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
                            return ValueError("Doesn't fit anywhere...")
        else:
             player.base_stats.add_stats(new_armor.stats) 
             self.armors.append(new_armor)
             self.equipped.append(new_armor)
             match new_armor.item_type:
                case "head":
                    self.head = new_armor
                    return
                case "chest":
                    self.chest = new_armor
                    return
                case "arms":
                    self.arms = new_armor
                    return
                case "legs":
                    self.legs = new_armor
                    return
                case _:
                    return ValueError("Doesn't fit anywhere..")

    def equip_weapon(self, unit, new_weapon):
        self.weapons.append(new_weapon)
        self.equipped.append(new_weapon)
        unit.base_stats.add_stats(new_weapon.stats)
        

    def unequip_weapon(self, unit, current_weapon):
        self.weapons.remove(current_weapon)
        self.add_to_bag(current_weapon)
        unit.base_stats.remove_stats(current_weapon.stats)
       

        
    def check_hands(self, player, new_weapon):
        wpn_count = len(self.weapons)

        if wpn_count == 0:
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
                    self.type_text(f"Swap {new_weapon.name} for {w.name}? (y/n)")
                    x = input()
                    if x in ["yes", "y"]:
                        self.unequip_weapon(player, w)
                        self.equip_weapon(player, new_weapon)
                        continue
                return
                

        if new_weapon.hands == 2:
            for w in self.weapons:
                self.unequip_weapon(player, w)
            self.equip_weapon(player, new_weapon)
            return

    def loot_body(self, player):
        for i in self.equipped:
            self.type_text(f"They dropped a {i.name}!!")
            self.type_text("Item stats:")
            i.stats.show_item_stats()
            self.type_text("Take it? (y/n)")
            take = input()
            looting = True
            while looting:
                if take in ["yes", "y"]:
                    self.equipped.remove(i)     
                    self.type_text("Bag or equip? (1/2)")
                    
                    bag_equip = input()
                    while True:
                        if bag_equip == "1":
                            if (len(self.bag)-1) >= 20:
                                self.type_text("Bag limit reached!")
                                self.type_text(f"{player.name} had to leave {i.name} behind...")
                                break
                            self.bag.remove(i)
                            player.inventory.add_to_bag(i)
                            break
                        elif bag_equip == "2":
                            player.inventory.equip_item(i, player)
                            break
                        else:
                            self.type_text("Unclear answer, try again")
                            bag_equip = input()
                            continue
                    break
                elif take in ["no", "n"]:
                    self.type_text("Oh well, your loss.")
                    break
                else:
                    self.type_text("Unclear answer, try again.")
                    take = input()
    

    def change_equipment(self, unit):
        i = 0
        self.type_text("Choose an item (number) to equip or toss:")
        for item in self.bag:
            self.type_text(f"{i+1}. {item.name}")
            item.stats.show_item_stats()
            self.type_text("")
            i += 1
        choice = int(input())
        while True:
            if choice > 0 and choice < len(self.bag):
                self.type_text(f"Equip or toss {self.bag[choice-1].name}? (e/t, or 'r' to return)")
                equip_toss = input()
                while True:
                    if equip_toss in ["e", "equip"]:
                        self.equip_item(self.bag[choice-1], unit)
                        self.bag.remove(self.bag[choice-1])
                        return
                    elif equip_toss in ["t", "toss"]:
                        self.throw_item(self.bag[choice-1])
                        return
                    elif equip_toss in ["r", "return"]:
                        return
                    else:
                        self.type_text("Unclear answer, try again")
                        equip_toss = input()
            else:
                self.type_text("Unclear answer, try again")
                item = input()
            break


    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")

