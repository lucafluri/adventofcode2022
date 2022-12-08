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
    visible = False
    # Check left
    for i in range(x-1, -1, -1):
        if forest[y][i] < h:
            count[0] += 1
        else: 
            visible = False
            break
    # Check right
    for i in range(x+1, len(forest[0])):
        if forest[y][i] < h:
            count[1] += 1
        else: 
            visible = False
            break
    # Check up
    for i in range(y-1, -1, -1):
        # print(x, i, forest[i][x], h)
        if forest[i][x] < h:
            count[2] += 1
        else: 
            visible = False
            break
    # Check down
    for i in range(y+1, len(forest)):
        if forest[i][x] < h:
            count[3] += 1
        else: 
            visible = False
            break
    # print(count, end=" ")
    # print(max(count) > 0)
    return (count[0] == x or count[1] == len(forest[0])-x-1 or count[2] == y or count[3] == len(forest)-y-1)
    

sum = 0
forest = []

for line in lines:
    forest.append([int(x) for x in line.strip()])
    
# Add outer trees
sum += len(forest)*2 + len(forest[0])*2 - 4



for x in range(1, len(forest[0])-1):
    for y in range(1, len(forest)-1):
        if(isVisible(x, y)):
            sum += 1

print(sum)

