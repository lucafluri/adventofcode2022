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
         1: {"l": 3, "p": [(0, 1), (1, 0), (2, 1), (1, 1), (1, 2)], "h": [2, 3, 2]},
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
    posX = 2
    length = rocks[id]["l"]
    
    # print("Drop", id, "at", posX, y, jetIndex)
    posX += jets[jetIndex]
    posX = max(0, min(7-length, posX))
    # print(posX, y, jetIndex)
    jetIndex = (jetIndex + 1) % len(jets)
    
    for i in range(2):
        y -= 1
        posX += jets[jetIndex]
        posX = max(0, min(7-length, posX))
        # print(posX, y, jetIndex)
        jetIndex = (jetIndex + 1) % len(jets)
        
    # y-=1

    # Check if there is a rock in the way
    while True:
        # Check and move down
        # Check jet push and check side and move
        # Repeat
        for i in range(length):
            # print(hRocks[posX + i], rocks[id]["p"][i][1]+y, y)
            # onBottom = rocks[id]["p"][i][1]+y == hRocks[posX + i]
            # TODO rock 1 (Cross) correct corner check
            onBottom = rocks[id]["p"][i][1]+y == hRocks[posX + i]
            # onside = rocks[id]["p"][i][0]+(posX+i-1) == hRocks[posX + i -1] or rocks[id]["p"][i][0]+(posX+i+1) == hRocks[posX + i +1]
            if(onBottom):
                # print("Rock on the way at x=", posX+i, "y=", y)
                # print("y=", rocks[id]["p"][i][1]+y)
                break
        else:
            if(y == 0):
                break
            y -= 1

            jet = jets[jetIndex]
            
            if(jet == -1): # Left
                if(posX == 0):
                    jet = 0
                elif(hRocks[posX-1] >= rocks[id]["p"][0][1]+y):
                    jet = 0
            elif(jet == 1):
                if(posX == 7-length):
                    jet = 0
                elif(hRocks[posX+length] >= rocks[id]["p"][0][1]+y):
                    jet = 0
            
            posX += jet
            # posX = max(0, min(7-length, posX))
            
            # print("::", posX, y, jetIndex)
            jetIndex = (jetIndex + 1) % len(jets)
            continue
        break
    
    # Add new top rocks 
    # print("posX", posX, "y", y)
    for i in range(length):
        hRocks[posX+i] = max(hRocks[posX+i], y + rocks[id]["h"][i])
    maxH = max(hRocks)
    # print(hRocks)


# Test drop 2
# hRocks = [18, 37, 37, 37, 37, 26, 25]
# hRocks = [0, 0, 0, 0, 1, 1, 0]
# jetIndex = 32
# should be [18, 37, 37, 37, 38, 39, 38]
# not
# Drop 1 at 2 40 32
# 3 40 32
# 2 39 33
# 3 38 34
# :: 4 37 35
# :: 3 36 36 ==> no execute
# Rock on the way at x= 3 y= 36
# [18, 37, 37, 38, 39, 38, 25]

# drop(0, hRocks)
# drop(1, hRocks)
# drop(2, hRocks)
# drop(3, hRocks)
# drop(4, hRocks)

# print(len(jets))
for i in range(2022):
    drop(i%5, hRocks)
    # print(jetIndex )
    
print(hRocks)
print(max(hRocks))
