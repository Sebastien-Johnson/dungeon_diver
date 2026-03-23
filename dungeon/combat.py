#combat system
import random
from systems.units import Monster, Player

class Combat():
    def __init__(self, combatant_1, combatant_2):
        self.combatant_1 = combatant_1
        self.combatant_2 = combatant_2
    
    def roll_initiative(self, combatant_1, combatant_2):
        if combatant_1.base_stats.agility > combatant_2.base_stats.agility:
            return combatant_1
        elif combatant_2.base_stats.agility > combatant_1.base_stats.agility:
            return combatant_2
        else:
            return random.choice([combatant_1, combatant_2])
        
    def combat_instance(self, player, monster): #setup as kwarg and iterate through users for multiplayer?
        first_attacker = self.roll_initiative(player, monster)
        if first_attacker == Player():
            self.choose_player_skill(player, monster)
            self.choose_monster_skill(monster, player)
        elif first_attacker == Monster():
            self.choose_monster_skill(monster, player)
            self.choose_player_skill(player, monster)
            

    def choose_player_skill(self, player, monster):
        skills_available = []
        skill_list = player.skills
        for skill in skill_list:
            if callable(getattr(skill_list, skill)):
                skills_available.append(skill)
                print(skill)
        print("Choose a skill to use this turn.")
        choice = input().lower()
        if choice in skills_available:
            choice(player, monster)
        

    def choose_monster_skill(self, monster, player):
        skills_available = []
        skill_list = monster.skills
        for skill in skill_list:
            if callable(getattr(skill_list, skill)):
                skills_available.append(skill(monster, player))
        return random.choice(skills_available)