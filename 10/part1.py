file = open('10/in.txt', 'r')
lines = file.readlines()

# Register: X, start: 1
# Two instructions: 
# - addx V => takes two cycles to add V to X (V can be negative)
# - noop takes one cycle, no effect

# signal strength (the cycle number multiplied by the value of the X register) 
# during the 20th cycle and every 40 cycles after that 
# (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

X = 1

l1 = []
l2 = []

s = []

for line in lines:
    line = line.strip().split(" ")
    if(line[0] == "addx"):
        l1.append(0)
        l1.append(int(line[1]))
    else:
        l1.append(0)

for i, n in enumerate(l1):
    l2.append(X*(i+1))
    print(i+1, X, X*(i+1))
    X += n
    

print(l1)
print(l2)

sum = l2[19] + l2[59] + l2[99] + l2[139] + l2[179] + l2[219]

print("20th cycle: ", l2[19])
print("60th cycle: ", l2[59])
print("100th cycle: ", l2[99])
print("140th cycle: ", l2[139])
print("180th cycle: ", l2[179])
print("220th cycle: ", l2[219])
print("Sum: ", sum)