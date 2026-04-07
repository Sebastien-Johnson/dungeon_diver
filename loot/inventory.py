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
        self.armor = []
        if self.head:
            self.armor.append(self.head[0])
        if self.chest:
            self.armor.append(self.chest[0])
        if self.arms:
            self.armor.append(self.arms[0])
        if self.legs:
            self.armor.append(self.legs[0])
        self.equipped = []
        for a in self.armor:
            self.equipped.append(a)
        for w in self.weapons:
            self.equipped.append(w)

    def add_to_bag(self, item):
        self.bag.append(item)

    def take_from_bag(self, item):
        self.bag.remove(item)

    def throw_item(self, item):
        self.bag.remove(item)
    
    def equip_item(self, item, player):
        if item == type(Equipment):
            self.equip_armor(item, player)
        elif item == type(Weapon):
            self.equip_weapon(item, player)

    def equip_armor(self, new_armor, player):
        for armor in self.armor:
            if new_armor.item_type == armor.item_type:
                player.stats.remove_stats(armor)
                player.stats.add_stats(new_armor)
                self.inventory.add_to_bag(armor)
                match new_armor.item_type:
                    case "head":
                        self.head = new_armor
                    case "chest":
                        self.chest = new_armor
                    case "arms":
                        self.arms = new_armor
                    case "legs":
                        self.legs = new_armor
            return
        else:
            print("Can't wear that there!")

    def equip_weapon(self, new_weapon, player):
        self.weapons.append(new_weapon)
        player.stats.add_stats(new_weapon)

    def unequip_weapon(self, player, current_weapon):
        self.weapons.remove(current_weapon)
        self.add_to_bag(current_weapon)
        player.stats.remove_stats(current_weapon)

        
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

    def loot_body(self, player):
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
