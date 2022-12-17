file = open('17/in2.txt', 'r')
line = file.readline()

# 7 slots wide, basically automated tetris, input loops
# Rocks appear, left edge at x=2 and bottom edge at 3 + highest rock/floor
# All rocks (Loop in this order):
# 
# ####
# 
# .#.
# ###
# .#.
# 
# ..#
# ..#
# ###
# 
# #
# #
# #
# #
# 
# ##
# ##
jets = []
for c in line:
    if c == '<':
        jets.append(-1)
    else: # c == '>'
        jets.append(1)
        
print(jets)
        
# Highest rocks of each column
hRocks = [0, 0, 0, 0, 0, 0, 0]
maxH = max(hRocks)
jetIndex = 0


# Idea shortcut jet pushes until highest rock, then check in more detail
y = maxH + 3
x = 2
jetSum = sum(jets[jetIndex:jetIndex+3])

length = 4

posX = min(7-length, max(0, x + jetSum))

print(posX)

