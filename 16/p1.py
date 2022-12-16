# Imports 
import re

file = open('16/in2.txt', 'r')
lines = file.readlines()

# Goal
# Release max pressure
# 1 min travel time, 1 min to release pressure
# What is max pressure releasable in 30 minutes?

# Idea
# Build graph with inverse weights from flow rate 
# BFS to build graph with distances from start
# DFS to find longest path on new graph

class Node:
    def __init__(self, name, flowrate):
        self.name = name
        self.flowrate = flowrate
        self.children = []
    
    def __eq__(self, other):
        return self.name == other.name
    
    # def __gt__(self, other):
    #     return self.flowrate > other.flowrate

    def __str__(self):
        return f"{self.name}, {self.flowrate}, {len(self.children)} children"
        
valves = []
    
regs = r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? ((\w\w,?[^\S\r\n]?)+)"

# Build Nodes
for line in lines:
    line = re.findall(regs, line)
    # print(line)
    n = Node(line[0][0], int(line[0][1]))
    # print(n)
    if n not in valves:
        valves.append(n)
    else:
        n = valves[valves.index(n)]
        n.flowrate = int(line[0][1])
    
    for c in line[0][2].split(', '):
        # print(c)
        c = Node(c, 0)
        if(c not in valves):
            valves.append(c)
        else:
            # print("Found")
            c = valves[valves.index(c)]
        n.children.append(c)
        

start = valves[valves.index(Node('AA', 0))]

opened = set()
currentNode = start
pressure = 0
minutes = 0



# def backtrack(node, minutes, pressure):

print(pressure)


    