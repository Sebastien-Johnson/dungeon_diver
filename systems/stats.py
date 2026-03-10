class Stats():
    def __init__(self, health=0, phys_armor=0, mag_armor=0, agility=0, mana=None, mag_pow=None, stamina=None, phys_pow=None):
        self.health = health
        self.phys_armor = phys_armor
        self.mag_armor = mag_armor
        self.agility = agility
        self.mana = mana
        self.mag_pow = mag_pow
        self.stamina = stamina
        self.phys_pow = phys_pow

    def lvl_up(self, health=0, phys_armor=0, mag_armor=0, agility=0, mana=None, mag_pow=None, stamina=None, phys_pow=None):
        self.health += health
        self.phys_armor += phys_armor
        self.mag_armor += mag_armor
        self.agility += agility
        self.check_has_stat("mana", mana)
        self.check_has_stat("mag_pow", mag_pow)
        self.check_has_stat("stamina", stamina)
        self.check_has_stat("phys_pow", phys_pow)   

    def check_has_stat(self, stat_name, stat):
        if self.stat_name:
            self.stat += stat
