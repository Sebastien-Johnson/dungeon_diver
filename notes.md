Roadmap
~~-separate unit classes from units~~
  ~~-set unit base stat by class~~
 ~~ -update game class~~
-monsters
  ~~-races~~
  ~~-tiers~~
~~-create "base stats" off class and race, scale leveling off base stats~~
-lvl system
  ~~-add xp~~
    ~~-lvl up~~
    ~~-xp overflow~~
  ~~-lvl bar~~
-Resource bars
  ~~-HP~~
  ~~-stam~~
  ~~-mana~~
  ~~-adding potions~~
  ~~-resting~~
  -dying
  ~~-taking damage/using resource~~
  
~~-Get xp from monster to player xp bar on death~~

~~-Monster skills~~
-dungeon lvl generation
  -monster generation
    ~~-Unique types arent creating new instances~~
  ~~-fix monster unit, class and race synergy~~
  ~~-lvl generation~~
  ~~-Announce monster turn and add wait before their attack~~
  ~~-skill selection~~
  -rest area every 10f
  -use items between combats attacking
  -use items after clearing a lvl
  -loot system
    -seperate weapon hands tracker and equip weapon function
  -xp update system
~~-basic abilities~~
 ~~ -use_ability function~~
  -ability library
  -add stamina cost to ability selection menu
-combat system
  ~~-list target health and caster resources after each attack~~
  -skill choice method
    ~~-add if monster~~
    ~~-add if attacking first or second~~
    ~~-add exit condition/while loop in dungeon level instance~~
    ~~-create list skills in skill classes to reference and iterate over~~
    ~~-create lvl locks on skills (initial if statement in each method that checks caster lvl)~~
  ~~-dmg calc~~
  -Add "return specs" method for skills for players to see
-update class bonuses to be multipliers instead of flat numbers
~~-xp scaling~~
-stat scaling
~~-item library~~
  ~~-item quality arg?~~
  


Notes
- Seperate initial stats, base stats and bonus stats (base+equipment)
- print item stats when asking to equip
  - print stat differences once equiped
- update die function to allow restart before sys exit
- add immediate leveling function to monster creation

 -'score' by XP obtained or dungeon lvl reached
  -Bonus for no damage instances
 -initiation and termination
 -save states?
 -multiplayer via socket library?
 -garbage cleaner


Outline
~~-classes~~
~~ -priest: healing, holy magic~~ 
 ~~-mage: high magic damage, elemental magic, squishy ~~
~~ -warrior: high defense ~~
~~ -ranger: high phys dmg, squishy~~
 -levels
  -lvl cap?

-abilities
 -elements
 -weaknesses/strengths
 -base dmg/multipliers
 -skill tree
 -accuracy

-loot
 -weapons
 -armor
 -potions
 -lootbag
  -throw away
  -give items
 -equipped items
  -equip after rounds
  -use after rounds for free

-monsters
 -monster generation based on party size, strength based on dungeon level
 -monster species: slime, bat, goblin, troll, 
 -intra species tiers: lesser, normal, greater, high 
 -intra species classes: priest, mage, warrior, ranger
 -xp model?

-dungeon levels
 -rest every 10 levels
 -use potions as turns
 -increasing difficulty
 -endless generation based on dungeon level

-turn based combat
 -calculating initiative
 -group combat
 -resolving missed abilities

-stats
 -health
 -mana/stamina
 -magic resistance
 -physical resistance
  -flat resistance model: 1 resistance = -1 damage