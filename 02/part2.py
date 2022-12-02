file1 = open('input.txt', 'r')
lines = file1.readlines()

# Rock, Paper, Scissors
# Rock > Scissors, 
# Scissors > Paper, 
# Paper > Rock

# Opponent: A => Rock, B => Paper, C => Scissors
# Outcome: X => Lose, Y => Draw, Z => Win


# Score Selection: 1 => Rock, 2 => Paper, 3 => Scissors +
# Total Score: 0 => Loss, 3 => Draw, 6 => Win

win = {'A': 2, 'B': 3, 'C': 1}
loss = {'A': 3, 'B': 1, 'C': 2}
tie = {'A': 1, 'B': 2, 'C': 3}

outcome = {'X': 0, 'Y': 3, 'Z': 6}

sum = 0
for line in lines:
    line = line.split()
    
    # outcome
    sum += outcome[line[1]]
    
    # Selection
    if(line[1] == 'Y'): sum += tie[line[0]]
    elif(line[1] == 'Z'): sum += win[line[0]]
    elif(line[1] == 'X'): sum += loss[line[0]]
    
print(sum)
    