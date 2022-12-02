file1 = open('input.txt', 'r')
lines = file1.readlines()

# Rock, Paper, Scissors
# Rock > Scissors, 
# Scissors > Paper, 
# Paper > Rock

# Opponent: A => Rock, B => Paper, C => Scissors
# Response: X => Rock, Y => Paper, Z => Scissors

#   X    Y    Z
# W C    A    B
# L B    C    A

# Score Selection: 1 => Rock, 2 => Paper, 3 => Scissors +
# Total Score: 0 => Loss, 3 => Draw, 6 => Win
win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
loss = {'X': 'B', 'Y': 'C', 'Z': 'A'}
tie = {'X': 'A', 'Y': 'B', 'Z': 'C'}

sum = 0
for line in lines:
    line = line.split()

    sum += ord(line[1])-87
        
    if(line[0] == tie[line[1]]): sum += 3 # Draw
    elif(line[0] == win[line[1]]): sum += 6
    
print(sum)
    