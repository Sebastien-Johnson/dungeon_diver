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
        
    def combat(self, combatant_1, combatant_2): #setup as kwarg and iterate through users for multiplayer?
        first_attacker = self.roll_initiative(combatant_1, combatant_2)
        if first_attacker == Player():
            self.choose_skill(combatant_1, combatant_2)

    def choose_skill(self, combatant_1, combatant_2):
        skills_available = []
        for skill in self.combat.skill_list:
            skills_available.append(skill)
            print(skill)
        print("Choose a skill to use this turn.")
        choice = input().lower()
        if choice in skills_available:
            combatant_1.skills.choice(combatant_1, combatant_2) 