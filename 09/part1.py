file = open('09/in.txt', 'r')
lines = file.readlines()

# Input is grid motion for head
# position of tail for every step of head
# H and T must be touching (all directions), can be in same spot
# Tail follows head if not touching
# H and T start off at same spot (0, 0)

# Answer: How many positions does the tail of the rope visit at least once?

visited = set() # set of visited positions (x, y) => tuples
visited.add((0, 0)) # start position
tPos = (0, 0) # current position of tail
hPos = (0, 0) # current position of head

move = {(0, -2): (0, -1), 
        (1, -2): (1, -1),
        (2, -2): (1, -1),
        (2, -1): (1, -1),
        (2, 0): (1, 0),
        (2, 1): (1, 1),
        (2, 2): (1, 1),
        (1, 2): (1, 1),
        (0, 2): (0, 1),
        }

def dist(t1, t2):
    return ((t1[0] - t2[0]), (t1[1] - t2[1]))

def add(t1, t2, invert=False):
    if(invert):
        return (t1[0] - t2[0], t1[1] + t2[1])
    return (t1[0] + t2[0], t1[1] + t2[1])

def setNewTailPosition():
    global hPos, tPos
    d = dist(hPos, tPos)
    
    # print('hPos: ', hPos, 'tPos: ', tPos, 'd: ', d)
   
    if(abs(d[0]) < 2 and abs(d[1]) < 2): # touching
        pass
    else: # not touching => move tail
        df  = (abs(d[0]), d[1])
        # print(d, move.get(d))
        tPos = add(tPos, move.get(df), d[0]<0)
        visited.add(tPos)
    # print('hPos: ', hPos)
        # print('tPos: ', tPos)
    # print('d: ', d, "\n")

def setHeadPos(dir, dist):
    global hPos
    if(dir == 'U'):
        hPos = (hPos[0], hPos[1] + dist)
    elif(dir == 'D'):
        hPos = (hPos[0], hPos[1] - dist)
    elif(dir == 'L'):
        hPos = (hPos[0] - dist, hPos[1])
    elif(dir == 'R'):
        hPos = (hPos[0] + dist, hPos[1])
    else:
        print('Error: Invalid direction')
        return
    
       

for line in lines:
    line = line.strip().split(' ') #[0] direction, [1] distance
    # print(line)
    for i in range(int(line[1])):  
        setHeadPos(line[0], 1)
        setNewTailPosition()
        
        
    
    
print(len(visited))
# print(visited)
    