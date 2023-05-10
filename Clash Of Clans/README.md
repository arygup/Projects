# Clash Of Clans On Terminal

- OOPs concepts in python to make a CoC game on terminal.

- To run the game : `python3 game.py`
- To view replays : `python3 replay.py`  and select the replay you want to watch according to mentioned date and time.
- For Victory : All buildings apart from walls get destroyed from the map in all three levels.
- For Defeat : If all troops and King die before destroying all buildings apart from walls.

## Unit Tests for the game :

- All appropriate comments have been added explaining each test.
- do note that each time code is executed the previous output gets deleted
- Tests for two different units of the provided codebase. Specifically  King.move(self, direction, V) & king.attack_target(self, target, attack)
- to run:               python3 test.py 
- output stored in:     output.txt
- to run:               python3 test_bonus.py
- output stored in:     output_bonus.txt

## Controls :

### Hero :

- w : move up
- a : move left
- d : move right
- s : move down
- 1 : Special Attack
- space : Normal Attack

### Barbarian :

- z : spawn at point 1
- x : spawn at point 2
- c : spawn at point 3

### Dragon :

- v : spawn at point 1
- b : spawn at point 2
- n : spawn at point 3

### Stealth Archers:

- 5 : spawn at point 1
- 6 : spawn at point 2
- 7 : spawn at point 3

### Healers

- 8 : spawn at point 1
- 9 : spawn at point 2
- 0 : spawn at point 3

### Archer :

- i : spawn at point 1
- o : spawn at point 2
- p : spawn at point 3

### Balloon :

- j : spawn at point 1
- k : spawn at point 2
- l : spawn at point 3

q : Quit Game

## Assumptions :

- Each building is randomly allocated a level between 1-5. For Wizard Tower & Cannon their levels effect the Attack & health properties.
- Each wall upon destruction, depending on its level explodes. Upon explosion each ground troop including King which is within coordinate +-2 of the wall will get a constant damage of 200.
- Rage and Heal Spell can be applied multiple times.
- The limit for troops in each level is as follows :
    - Barbarians : 10
    - Archers : 7
    - Balloon : 5
    - Dragon : 3
- You have to choose the type of troop movement at start of the game.
- You have to choose the hero after each level.
