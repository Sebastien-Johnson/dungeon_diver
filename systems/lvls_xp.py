#lvl and xp system
"""
-current xp
-xp needed to lvl up
-adding new xp
    -lvl up
    -xp overflow
    -new xp_to_lvl calc
    -incrementing player level and stats
    -unlocking abilities
-separate lvling class? create new xp bar obj on lvl?
"""

class ExpBar():
    def __init__(self, xp_to_lvl, current_xp=0):
        self.xp_to_lvl = xp_to_lvl
        self.current_xp = current_xp
    
        
class Leveling():
    def __init__(self):
        self.xp_bar = ExpBar()

    def add_xp(self, new_xp):
        self.xp_bar.current_xp += new_xp
        if self.xp_bar.current_xp >= self.xp_bar.xp_to_lvl:
            self.lvl_up

    def lvl_up(self):
        extra_xp = self.xp_bar.current_xp - self.xp_bar.xp_to_lvl
        self.xp_bar = ExpBar(self.xp_bar.xp_to_lvl, 0)
        self.add_xp(extra_xp)