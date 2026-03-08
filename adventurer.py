class Adventurer():
    def __init__(self, name, health, phys_armor, mag_armor, agility):
        self.name = name
        self.health = health
        self.phys_armor = phys_armor
        self.mag_armor = mag_armor
        self.agility = agility
        #abilities
        #equipment

    
class Warrior(Adventurer):
    def __init__(self, name, health, phys_armor, mag_armor, agility, stamina, phys_pow):
        super().__init__(name, health, phys_armor, mag_armor, agility)
        self.stamina = stamina
        self.phys_pow = phys_pow


class Cleric(Adventurer):
    def __init__(self, name, health, phys_armor, mag_armor, agility, stamina, phys_pow):
        super().__init__(name, health, phys_armor, mag_armor, agility)
        self.stamina = stamina
        self.phys_pow = phys_pow

class Ranger(Adventurer):
    def __init__(self, name, health, phys_armor, mag_armor, agility, stamina, phys_pow):
        super().__init__(name, health, phys_armor, mag_armor, agility)
        self.stamina = stamina
        self.phys_pow = phys_pow

class Mage(Adventurer):
    def __init__(self, name, health, phys_armor, mag_armor, agility, mana, mag_pow):
        super().__init__(name, health, phys_armor, mag_armor, agility)
        self.mana = mana
        self.mag_pow = mag_pow