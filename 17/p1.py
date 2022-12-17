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
    y = maxH + 1
    x = 2

    upper = (jetIndex + 3 )% len(jets)
    jetSum = sum(jets[jetIndex:upper])
    jetIndex += 3
    length = rocks[id]["l"]

    # bottom left corner
    # Go to +1 of highest rock
    posX = min(7-length, max(-2, x + jetSum))
    # if(jetSum < -2): jetsum = -2
    # if(jetSum > (7-length)-2): jetSum = 7-length-2

    # print(posX)
    # print(x, y)

 
    # Check if there is a rock in the way
    while True:
        # print(x, y)
        for i in range(posX, posX+length):
            if(maxH != 0 and hRocks[i] == rocks[id]["p"][i][1]+1 or y == 0):
                print("Rock in the way", i, hRocks[i], rocks[id]["p"][i][1] -1, y)
                
                break
            else:
               pass
        else:
            y -= 1
            posX += jets[jetIndex]
            print(posX)
            jetIndex = (jetIndex + 1) % len(jets)
            posX = min(7-length, max(-2, posX))
            continue
        break

    # Add new top rocks # !! TODO per rock different
    for x in range(posX, posX+length):
        hRocks[x] = max(hRocks[x], y + rocks[id]["h"][x-posX])
    print(hRocks)


drop(0, hRocks)
drop(1, hRocks)
# drop(2, hRocks)
print(hRocks)
