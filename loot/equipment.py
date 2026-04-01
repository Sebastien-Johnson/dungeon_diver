from .items_base import *

class Inventory():
    def __init__(self):
        self.bag = []
        self.head = HeadPiece
        self.chest = ChestPiece
        self.legs = LegPiece
        self.arms = ArmPiece
        self.weapons = [Weapon]
        self.armor = [self.head, self.chest, self.legs, self.arms]

    def add_to_bag(self, item):
        self.bag.append(item)

    def take_from_bag(self, item):
        self.bag.remove(item)

    def throw_item(self, item):
        self.bag.remove(item)

    def equip_armor(self, player, body_part, current_armor, new_armor):
        if current_armor.item_type == new_armor.item_type:
            player.stats.remove_stats(current_armor)
            player.stats.add_stats(new_armor)
            self.inventory.add_to_bag(current_armor)
            match body_part:
                case "head":
                    self.head = new_armor
                case "chest":
                    self.chest = new_armor
                case "arms":
                    self.arms = new_armor
                case "legs":
                    self.legs = new_armor
        else:
            print("Can't wear that there!")

    def equip_weapon(self, player, new_weapon):
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
    
