#combat system
import random, time
from systems.units import Monster, Player

class Combat():
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
    
    def roll_initiative(self, player, monster):
        if player.base_stats.agility > monster.base_stats.agility:
            return player
        elif monster.base_stats.agility > player.base_stats.agility:
            return monster
        else:
            print("random")
            return random.choice([player, monster])
        
    def combat_instance(self, player, monster): #setup as kwarg and iterate through users for multiplayer?
        first_attacker = self.roll_initiative(player, monster)
        if first_attacker == player:
            self.choose_player_skill(player, monster)
            time.sleep(1)
            if monster.base_stats.current_health > 0:
                self.choose_monster_skill(monster, player)
        elif first_attacker == monster:
            self.choose_monster_skill(monster, player)
            time.sleep(1)
            self.choose_player_skill(player, monster)
            

    def choose_player_skill(self, player, monster):
        print("Choose a skill to use this turn.")
        print(f"Skills available: {player.skills.skill_list}")    
        player_choice = input().lower()
        propper_choice = False

        while propper_choice == False:
            if f"{player_choice}" in player.skills.skill_list:
                propper_choice = True
                time.sleep(1)
                getattr(player.skills, f"{player_choice}")(player, monster)
            else:
                print(f"Sorry, '{player_choice}' is not a skill you know. Try again.\n")
                player_choice = input().lower()
       
        

    def choose_monster_skill(self, monster, player):
        monster_choice = random.choice(monster.skills.skill_list)
        getattr(monster.skills, f"{monster_choice}")(monster, player)