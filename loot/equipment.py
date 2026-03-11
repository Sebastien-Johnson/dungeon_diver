from items import Item, Weapon, Armor

class Inventory():
    def __init__(self):
        self.bag = []
        self.head = Item
        self.chest = Item
        self.legs = Item
        self.arms = Item
        self.weapons = []
        self.equipped = [self.head, self.chest, self.legs, self.arms, self.weapons]

    def add_to_bag(self, item=Item):
        self.bag.append(item)

    def throw_item(self, item=Item):
        self.bag.remove(item)

    def give_item(self, player, item=Item):
        player.inventory.add_to_bag(item)
        self.throw_item(item)

    def equip_armor(self, body_part, current_armor=Armor, new_armor=Armor):
        if current_armor.item_type == new_armor.item_type:
            self.inventory.add_to_bag(current_armor)
            body_part = new_armor
        else:
            print("Can't wear that there!")

    def equip_weapon(self, new_weapon=Weapon):
        wpn_count = len(self.weapons)

        if wpn_count == 0:
            self.weapons.append(new_weapon)
            return
        
        if new_weapon.hands == 1:
            if wpn_count == 1:
                if self.weapons[0].hands == 1:
                    self.weapons.append(new_weapon)
                    return
                else:
                    self.inventory.add_to_bag(self.weapons[0])
                    self.weapons.append(new_weapon)
                    return
                
            if wpn_count == 2: 
                for w in self.weapons:
                    print(f"Swap {new_weapon.name} for {w.name}?")
                    x = input()
                    if x == "yes":
                        self.inventory.add_to_bag(self.weapons[0])
                        self.weapons.append(w)
                        return
                

        if new_weapon.hands == 2:
            for w in self.weapons:
                self.inventory.add_to_bag(w)
            self.weapons.append(new_weapon)
        
