//Wumpus World

import random

# -------- USER INPUT --------
GRID_SIZE = int(input("Enter grid size (4,5,6...): "))
MAX_ACTIONS = int(input("Enter maximum actions: "))

ax = int(input("Enter agent starting row: "))
ay = int(input("Enter agent starting column: "))

agent = [ax, ay]

# -------- RANDOM POSITION --------
def random_position():
    return (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

# -------- PLACEMENT --------
while True:
    gold = random_position()
    if gold != tuple(agent): break

while True:
    wumpus = random_position()
    if wumpus != tuple(agent) and wumpus != gold: break

pits = []
num_pits = GRID_SIZE // 2
while len(pits) < num_pits:
    p = random_position()
    if p != tuple(agent) and p != gold and p != wumpus and p not in pits:
        pits.append(p)

gold_collected = False
wumpus_alive = True
arrow_available = True

# -------- UPDATED DISPLAY GRID (GOD MODE) --------
def display_grid(cheat=False):
    if cheat:
        print("\n--- MASTER MAP (GOD MODE) ---")
    else:
        print("\nAgent World View")

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell = " . "
            if [i, j] == agent:
                cell = " A "
            elif cheat:
                if (i, j) == gold and not gold_collected:
                    cell = " G "
                elif (i, j) == wumpus and wumpus_alive:
                    cell = " W "
                elif (i, j) in pits:
                    cell = " P "

            print(cell, end="")
        print()
    print()

# -------- SENSORS & ACTIONS (Keep original logic) --------
def get_sensors(bump=False, scream=False):
    x, y = agent
    sensors = []
    for p in pits:
        if abs(p[0]-x) + abs(p[1]-y) == 1: sensors.append("Breeze")
    if wumpus_alive and abs(wumpus[0]-x) + abs(wumpus[1]-y) == 1:
        sensors.append("Stench")
    if (x, y) == gold and not gold_collected: sensors.append("Glitter")
    if bump: sensors.append("Bump")
    if scream: sensors.append("Scream")
    return sensors

def move(direction):
    x, y = agent
    bump = False
    if direction == "UP": x -= 1
    elif direction == "DOWN": x += 1
    elif direction == "LEFT": y -= 1
    elif direction == "RIGHT": y += 1

    if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
        bump = True
    else:
        agent[0], agent[1] = x, y
    return bump

def shoot():
    global wumpus_alive, arrow_available
    if not arrow_available:
        print("No arrows left")
        return False
    arrow_available = False
    if agent[0] == wumpus[0] or agent[1] == wumpus[1]:
        wumpus_alive = False
        print("Arrow hit the Wumpus!")
        return True
    print("Arrow missed")
    return False

def check_status():
    pos = tuple(agent)
    if pos in pits:
        print("Agent fell into PIT. GAME OVER")
        return True
    if pos == wumpus and wumpus_alive:
        print("Wumpus ate the agent. GAME OVER")
        return True
    return False

# -------- GAME START --------
print("\n===== WUMPUS WORLD =====")
# Reveal map at the start for debugging
display_grid(cheat=True)

actions = 0
while actions < MAX_ACTIONS:
    bump, scream = False, False
    sensors = get_sensors()
    print(f"Current Position: ({agent[0]}, {agent[1]})")
    print("Sensors:", sensors)

    action = input("Action (UP,DOWN,LEFT,RIGHT,GRAB,SHOOT,CLIMB): ").upper()

    if action in ["UP","DOWN","LEFT","RIGHT"]:
        bump = move(action)
    elif action == "GRAB":
        if tuple(agent) == gold:
            gold_collected = True
            print("Gold grabbed!")
        else:
            print("No gold here")
    elif action == "SHOOT":
        scream = shoot()
    elif action == "CLIMB":
        if gold_collected and agent == [ax, ay]:
            print("Agent climbed out with GOLD. SUCCESS!")
            break
        else:
            print("Condition failed: Start at", [ax, ay], "with gold collected.")
    else:
        continue

    actions += 1
    display_grid(cheat=False) # Keep normal view during play
    if check_status(): break
else:
    print("Maximum actions reached. GAME OVER")



