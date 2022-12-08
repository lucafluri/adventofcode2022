import numpy as np
file = open('in.txt', 'r')
lines = file.readlines()

# Count trees being visible from the outside of the matrix
# For each tree count in all directions if there is a tree
# higher than the current tree. All trees on the edge are visible
# Count visible trees

def isVisible(x, y):
    h = forest[y][x]
    # print("Checking tree at " + str(x) + ", " + str(y) + " with height " + str(h))
    
    
    count = [0, 0, 0, 0] # left, right, up, down
    # Check left
    for i in range(x-1, -1, -1):
        count[0] += 1
        if(forest[y][i] >= h):
            break
    # Check right
    for i in range(x+1, len(forest[0])):
        count[1] += 1
        if(forest[y][i] >= h):
            break
    # Check up
    for i in range(y-1, -1, -1):
        # print(x, i, forest[i][x], h)
        count [2] += 1
        if(forest[i][x] >= h):
            break
        
    # Check down
    for i in range(y+1, len(forest)):
        count [3] += 1
        if(forest[i][x] >= h):
            break
    # print(count)
    # return (count[0] == x or count[1] == len(forest[0])-x-1 or count[2] == y or count[3] == len(forest)-y-1)
    sScore = np.prod(count, where=[x > 0 for x in count])
    # print(sScore)
    return sScore
    

sum = 0
forest = []

for line in lines:
    forest.append([int(x) for x in line.strip()])
    
# Add outer trees
# sum += len(forest)*2 + len(forest[0])*2 - 4


maxScore = 0
for x in range(1, len(forest[0])-1):
    for y in range(1, len(forest)-1):
        if(isVisible(x, y) > maxScore):
            maxScore = isVisible(x, y)
print(maxScore)

