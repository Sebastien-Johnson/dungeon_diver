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
    def __init__(self, xp_to_lvl):
        self.xp_to_lvl = xp_to_lvl
        self.current_xp = 0
    
        
class Leveling():
    def __init__(self):
        self.xp_bar = ExpBar()
        self.current_lvl = 1

    def add_xp(self, new_xp):
        self.xp_bar.current_xp += new_xp
        if self.xp_bar.current_xp >= self.xp_bar.xp_to_lvl:
            self.lvl_up()

    def lvl_up(self):
        extra_xp = self.xp_bar.current_xp - self.xp_bar.xp_to_lvl
        self.xp_bar = ExpBar(self.xp_to_next(self.current_lvl))
        self.current_lvl += 1
        self.add_xp(extra_xp)
        

    def xp_to_next(self, current_lvl):
        xp_base = 100
        xp_multiplier = 1.25
        next_lvl = current_lvl + 1
        xp_to_next = xp_base*xp_multiplier*(next_lvl-1)
        return xp_to_next
