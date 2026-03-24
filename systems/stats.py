class Stats():
    def __init__(self, max_health=0, phys_armor=0, mag_armor=0, agility=0, max_mana=0, mag_pow=0, max_stamina=0, phys_pow=0):
        self.max_health = max_health
        self.current_health = max_health
        self.phys_armor = phys_armor
        self.mag_armor = mag_armor
        self.agility = agility
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.mag_pow = mag_pow
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina
        self.phys_pow = phys_pow 

    def add_stats(self, new_stats):
        self.max_health += new_stats.max_health
        self.phys_armor += new_stats.phys_armor
        self.mag_armor += new_stats.mag_armor
        self.agility += new_stats.agility
        self.max_mana += new_stats.max_mana
        self.mag_pow += new_stats.mag_pow
        self.max_stamina += new_stats.max_stamina
        self.phys_pow += new_stats.phys_pow

    