fileIn = open("12/in.txt", 'r')
lines = fileIn.readlines()

# Height map from a to z (low to high)
# Current Pos: S (a)
# Goal pos: E (z)
# Find shortest path from S to E
# Can move in NESW directions
# Next step at most one higher, low doesn't matter

# Idea:
# Build adjancy matrix of legal moves
# BFS from S to E

start = None
end = None
class Node:
    def __init__(self, name):
        global start, end
        self.name = name
        self.adj = []
        self.dist = 0 # to start
        self.visited = False
        self.height = ord(name)
        if(self.name == 'S'):
            self.height = ord('a')
            start = self
        elif(self.name == 'E'):
            self.height = ord('z')
            end = self
    
    def __str__(self):
        return self.name 


# read input as matrix
nodes = []
inputMatrix = []

for line in lines:
    line = line.strip()
    inputMatrix.append([Node(c) for c in line])
    for c in inputMatrix[-1]:
        nodes.append(c)

# print(inputMatrix)

# Build adjacency matrix

def addtoAdj(x, y):
    t = inputMatrix[x][y]
    # print(x, y, t)
    if(x > 0): 
        N = inputMatrix[x-1][y]
        if(N.height <= t.height + 1):
            t.adj.append(N)
            
    if(y < len(inputMatrix[0])-1): 
        E = inputMatrix[x][y+1]
        if(E.height <= t.height + 1):
            t.adj.append(E)
            
    if(x < len(inputMatrix)-1): 
        S = inputMatrix[x+1][y]
        if(S.height <= t.height + 1):
            t.adj.append(S)
            
    if(y > 0):
        W = inputMatrix[x][y-1]
        if(W.height <= t.height + 1):
            t.adj.append(W)
            
for x in range(len(inputMatrix)):
    for y in range(len(inputMatrix[0])):
        # print(inputMatrix[x][y])
        # print(inputMatrix[x][y-1])
        addtoAdj(x, y)

# for n in nodes:
    # print(n, n.adj)

queue = [start]
# visited = set()

while(len(queue) != 0):
    node = queue.pop(0)
    for n in node.adj:
        if(not n.visited):
            n.dist = node.dist + 1
            n.visited = True
            queue.append(n)

print(end.dist)
