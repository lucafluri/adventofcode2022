file1 = open('input.txt', 'r')
lines = file1.readlines()

# Build list of stacks from input
# Parse move instructions
# Get top containers to move as sublist, reverse and add to new stack
# print all top containers of all stacks as puzzle answer

# Get number of stacks
lineStart = 0
numberOfStacks = 0

# Get line number of first move
for i, line in enumerate(lines):
    if(line.startswith('move')): 
        lineStart = i
        break

# Create list of stacks
numberOfStacks = lines[lineStart-2].strip()[-1]
stacks = [[] for i in range(int(numberOfStacks))]
print(numberOfStacks)

# [R] [H] [N] [P] [J] [Q] [B] [C] [F]
#  1   2   3   4   5   6   7   8   9 
# 01234567890123456789012345678901234
# 1-1, 2-5, 3-9, 4-13, 5-17, 6-21, 7-25, 8-29, 9-33
# Y = 4*X - 3, X = (Y + 3)/4

# Iterate over start stacks and add containers to stacks
for i, line in enumerate(lines):
    if(line.strip()[0].isdigit()): break;
    
    line = line.replace('[', ' ').replace(']', ' ')

    for j, c in enumerate(line):
        if(c.isalpha()):
            idx = int((j + 3)/4)-1          
            stacks[idx].insert(0, c)
            
print(stacks)

# Parse and execute move instructions
for line in lines[lineStart:]:
    line = line.replace('move', '').replace('from', '').replace('to', '').replace('  ', ' ')
    line = line.strip().split(' ')
    
    x = int(line[0])
    a = int(line[1])-1
    b = int(line[2])-1
    
    toMove = stacks[a][-x:]
    toMove.reverse()
    stacks[b].extend(toMove)
    stacks[a] = stacks[a][:-x]
            
    
    
for s in stacks:
    print(s[-1], end='')