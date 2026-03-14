#dungeon generation system
class Dungeon():
    def __init__(self, player):
        self.player = player
        self.curent_lvl = DungeonLvl()

    def next_dungeon_lvl(self):
        self.curent_lvl = DungeonLvl()
        #check if current lvl is rest area
        #allow for potions between levels

class DungeonLvl():
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster #generate random monster

    def start_combat(self, player, monster):
        #combat class goes back and forth allowing players to select abilities and monsters randomly choose 
        while player.stats.current_health > 0 and monster.stats.current_health >0:
            if player.stats.agility > monster.stats.current_health:
                pass
                #player uses ability 
                #monster uses ability
            elif monster.stats.current_health > player.stats.current_health >0:
                pass
                #monster uses ability
                #player uses ability
            else:
                pass
                #randomly chooses first attacker
    