file1 = open('input.txt', 'r')
lines = file1.read()
lines = lines.split("\n\n")

# Part I
sums = []

for line in lines:
    line = line.split("\n")
    s = 0;
    for cal in line:
        s += int(cal)
    sums.append(s)

print(max(sums))