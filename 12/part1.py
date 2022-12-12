fileIn = open("12/in2.txt", 'r')
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

# read input as matrix
inputMatrix = []

for line in lines:
    line = line.strip()
    inputMatrix.append([c for c in line])

# Build adjacency matrix
adjMat = []

def addtoAdj(x, y):
