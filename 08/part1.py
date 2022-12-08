file = open('in.txt', 'r')
lines = file.readlines()

# Count trees being visible from the outside of the matrix
# For each tree count in all directions if there is a tree
# higher than the current tree. All trees on the edge are visible
# Count visible trees

def isVisible(x, y):
    h = forest[x][y]
    
    count = 0
    # Check left
    for i in range(x-1, -1, -1):
        if forest[i][y] < h:
            return True
    # Check right
    for i in range(x+1, len(forest[0])):
        if forest[i][y] < h:
            return True
    # Check up
    for i in range(y-1, -1, -1):
        if forest[x][i] < h:
            return True
    # Check down
    for i in range(y+1, len(forest)):
        if forest[x][i] < h:
            return True
    return False
    

sum = 0
forest = []

for line in lines:
    forest.append([int(x) for x in line.strip()])
    
# Add outer trees
sum += len(forest)*2 + len(forest[0])*2 - 4



for x in range(len(forest[0])):
    for y in range(len(forest)):
        if(isVisible(x, y)):
            sum += 1

print(sum)

