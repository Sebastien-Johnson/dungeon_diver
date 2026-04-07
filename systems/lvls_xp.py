import time

class ExpBar():
    def __init__(self, xp_to_lvl):
        self.xp_to_lvl = xp_to_lvl
        self.current_xp = 0
    
        
class Leveling():
    def __init__(self):
        self.xp_bar = ExpBar(100)
        self.current_lvl = 1

    def add_xp(self, player, new_xp):
        self.xp_bar.current_xp += new_xp
        if self.xp_bar.current_xp >= self.xp_bar.xp_to_lvl:
            old_stats = player.base_stats
            self.lvl_up()
            player.base_stats.show_stat_update(old_stats)

    def lvl_up(self):
        extra_xp = self.xp_bar.current_xp - self.xp_bar.xp_to_lvl
        self.xp_bar = ExpBar(self.xp_to_next(self.current_lvl))
        self.current_lvl += 1
        self.add_xp(extra_xp)
        self.type_text("Level up!!")
        self.type_text(f"Level: {self.current_lvl-1} -> {self.current_lvl}\n")
        

    def xp_to_next(self, current_lvl):
        xp_base = 100
        xp_multiplier = 1.25
        next_lvl = current_lvl + 1
        xp_to_next = xp_base*xp_multiplier*(next_lvl-1)
        return xp_to_next
    
    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")
