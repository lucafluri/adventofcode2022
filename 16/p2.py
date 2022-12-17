# Imports 
import re

file = open('16/in2.txt', 'r')
lines = file.readlines()

# Goal
# Release max pressure
# 1 min travel time, 1 min to release pressure
# What is max pressure releasable in 30 minutes?

nodes = set()
flowrates = {}
distances = {}
children = {}

regs = r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? ((\w\w,?[^\S\r\n]?)+)"

# Build Nodes
for line in lines:
    line = re.findall(regs, line)
    # print(line)
    name = line[0][0]
    fr = int(line[0][1])
    # print(n)
    nodes.add(name)
    children[name] = []
    flowrates[name] = fr
    for c in line[0][2].split(','):
        children[name].append(c.strip())
        
print("Starting BFS")
# Calc all distances between nodes with flowrates > 0
for start in nodes:
    visited = set()
    queue = [start]
    distances[start] = {start: 0}
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for child in children[node]:
                if child not in distances[start]:
                    distances[start][child] = distances[start][node] + 1
                queue.append(child)

# Find all possible paths in 30 minutes
# DFS for all paths
def findPaths(distances, flowrates):
    paths = []
    pressures = []

    print("Starting DFS")
    # time, press, path
    stack = [(26, 0, ['AA'])]
    while len(stack) > 0:
        # print(stack)
        t, p, path = stack.pop()
        current = path[-1]
        possibleStates = []
        for n, d in distances[current].items():
            # No time left or already visited
            if(n in path or d+2>t or flowrates[n] == 0): # time to open and letting pressure out
                continue
            newTime = t - d - 1
            newPressure = p + flowrates[n] * newTime
            newState = (newTime, newPressure, path + [n])
            possibleStates.append(newState)

        if(len(possibleStates) > 0):
            stack.extend(possibleStates)
        else: #exhausted search direction
            pressures.append(p)
            paths.append(path[1:])
    return paths, pressures
            

# Best path for me
# paths, pressures = findPaths(distances, flowrates)

# Find 2 path with no overlap and max pressure
allPaths = list(zip(*findPaths(distances, flowrates)))
allPaths.sort(reverse=True, key=lambda x: x[1])
paths, pressures = zip(*allPaths)

# print(paths, pressures)
# print(any(x in [1, 2, 3] for x in [4, 5, 5]))

a, b = 0, 1 # indexes of paths for me and elephant
max = 0

for pA in paths[:1000]:
    for pB in paths[:1000]:
        # print(pA, pB)
        if(pA != pB):
            for x in pA:
                if(x in pB):
                    break
            pressure = pressures[paths.index(pA)] + pressures[paths.index(pB)]
            if(pressure > max):
                print(pressure, pA, pB)
                max = pressure
        
        
        # if(pA != pB and not any(x in pA for x in pB)):
        #     print("Found")
            

print(max)

# while(any(x in paths[a] for x in paths[b])):
#     b += 1
#     if(b >= len(paths)):
#         a += 1
#         b = a + 1
#     if(a >= len(paths)):
#         break
# if(pressures[a] + pressures[b] > max):
#     max = pressures[a] + pressures[b]
    # print(max, a, b, allPaths[a][1], allPaths[b][1])
# print(any([x in allPaths[a] for x in allPaths[b]]))
