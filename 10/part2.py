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
crt = ""

s = []

for line in lines:
    line = line.strip().split(" ")
    if(line[0] == "addx"):
        l1.append(0)
        l1.append(int(line[1]))
    else:
        l1.append(0)

for i, n in enumerate(l1):
    if(i%40 in [X-1, X, X+1]):
        crt += ('#')
    else:
        crt +=('.')
    X += n


for i,  n in enumerate(crt):
    print(n, end='')
    if(i in [39, 79, 119, 159, 199, 239]):
        print()