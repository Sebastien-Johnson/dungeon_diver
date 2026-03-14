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
-dungeon lvl generation
  -monster generation
  -lvl generation
  -rest area every 10f
  -use items instead of attacking
  -use items after clearing a lvl
  -loot system
  -xp update system
-basic abilities
  -use_ability function
  -ability library
-combat system
  -dmg calc
-xp scaling
-stat scaling
-elemental system
  -enchantment effects
  -dmg modifiers
-item library
-update die function to allow restart before sys exit


Notes
 -initiation and termination
 -save states?
 -multiplayer via socket library?


Outline
-classes
 -priest: healing, holy magic 
 -mage: high magic damage, elemental magic, squishy 
 -warrior: high defense 
 -ranger: high phys dmg, squishy
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

-montsters
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