from player_races import Race
from units import Monster
#monster races

def monster_tier(tier, monster_name):
    new_name = f"{tier} {monster_name}"
    return new_name


class Slime(Monster):
    def __init__(self, name, race, unit_class, lvl):
        super().__init__(name, race, unit_class, lvl)


