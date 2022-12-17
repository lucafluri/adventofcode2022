# Imports 
import re

file = open('16/in.txt', 'r')
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
paths = []
pressures = []

print("Starting DFS")
# time, press, path
stack = [(30, 0, ['AA'])]
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
            



        
# print(nodes)
# print(children)
# print(flowrates)
# for n, d in distances.items():
#     print(n, d)
# print(paths)
# idx = pressures.index(max(pressures))
# print(pressures[idx])
# print(paths[idx])
print(max(pressures))
# print(distances['AA']['CC'])
