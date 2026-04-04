#combat system
import random, time

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
        self.type_text("Choose a skill (number) to use this turn.")
        self.type_text(f"Skills available:")
        for key, value in player.skills.skill_list.items():
            self.type_text(f"{key}. {value}")   
        player_choice = input().lower()
        propper_choice = False

        while propper_choice == False:
            if f"{player_choice}" in player.skills.skill_list:
                propper_choice = True
                time.sleep(1)
                getattr(player.skills, player.skills.skill_list[f"{player_choice}"])(player, monster)
            else:
                self.type_text(f"Sorry, '{player_choice}' is not a skill you know. Try again.")
                player_choice = input().lower()
       
        

    def choose_monster_skill(self, monster, player):
        monster_choice = random.choice(monster.skills.skill_list)
        getattr(monster.skills, f"{monster_choice}")(monster, player)

    def type_text(self, text_string):
        for t in text_string:
            print(f"{t}", end="", flush=True)
            time.sleep(.04)
        print("")
        