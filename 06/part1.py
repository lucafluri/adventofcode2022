file1 = open('input.txt', 'r')
line = file1.read()

# Find first index character after four different characters in lines
idx = 4
s = line[idx-4:idx]
while(len(s) != len(set(s))):
    idx += 1
    s = line[idx-4:idx]

print(idx)

