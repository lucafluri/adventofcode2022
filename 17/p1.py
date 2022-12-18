file = open('17/in2.txt', 'r')
line = file.readline()

# 7 slots wide, basically automated tetris, input loops
# Rocks appear, left edge at x=2 and bottom edge at 3 + highest rock/floor
# All rocks (Loop in this order):
# 
# ####
# 
# .#.
# ###
# .#.
# 
# ..#
# ..#
# ###
# 
# #
# #
# #
# #
# 
# ##
# ##
jets = []
for c in line:
    if c == '<':
        jets.append(-1)
    else: # c == '>'
        jets.append(1)
        
# print(jets)

# 0, 0 alsways bottom left
rocks = {0: {"l": 4, "p": [(0, 0), (1, 0), (2, 0), (3, 0)], "h": [1, 1, 1, 1]},
         1: {"l": 3, "p": [(1, 0), (0, 1), (2, 1), (1, 1), (1, 2)], "h": [2, 3, 2]},
         2: {"l": 3, "p": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], "h": [1, 1, 3]},
         3: {"l": 1, "p": [(0, 0), (0, 1), (0, 2), (0, 3)], "h": [4]},
         4: {"l": 2, "p": [(0, 0), (1, 0), (0, 1), (1, 1)], "h": [2, 2]}}
        
# Highest rocks of each column
hRocks = [0, 0, 0, 0, 0, 0, 0]

jetIndex = 0

# Idea shortcut jet pushes until highest rock, then check in more detail

def drop(id, hRocks):
    global jetIndex, jets
    maxH = max(hRocks)
    y = maxH+3
    x, posX = 2, 2
    length = rocks[id]["l"]
    
    
    posX += jets[jetIndex]
    posX = max(0, min(7-length, posX))
    jetIndex = (jetIndex + 1) % len(jets)
    # print(posX, y, jetIndex)
    for i in range(3):
        y -= 1
        posX += jets[jetIndex]
        posX = max(0, min(7-length, posX))
        jetIndex = (jetIndex + 1) % len(jets)
        # print(posX, y, jetIndex)
    # y-=1

    # Check if there is a rock in the way
    while True:
        for i in range(length):
            # TODO check before move and break if there is a rock
            # !!
            onBottom = hRocks[posX + i] == rocks[id]["p"][i][1]+y
            onside = rocks[id]["p"][i][0]+(posX+i-1) == hRocks[posX + i -1] or rocks[id]["p"][i][0]+(posX+i+1) == hRocks[posX + i +1]
            if(onBottom or onside):
                # print("Rock on the way at x=", posX+i, "y=", y, onBottom, onside)
                # print("y=", rocks[id]["p"][i][1]+y)
                break
        else:
            posX += jets[jetIndex]
            posX = max(0, min(7-length, posX))
            jetIndex = (jetIndex + 1) % len(jets)
            y -= 1
            # print(posX, y, jetIndex)
            continue
        break
    
    # Add new top rocks 
    for i in range(length):
        hRocks[posX+i] = max(hRocks[posX+i], y + rocks[id]["h"][i])
    maxH = max(hRocks)
    # print(hRocks)


drop(0, hRocks)
drop(1, hRocks)
drop(2, hRocks)

for i in range(0, 4):
    drop(i%5, hRocks)
print(hRocks)
print(max(hRocks))
