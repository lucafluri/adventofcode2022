file1 = open('input.txt', 'r')
lines = file1.readlines()

# Find common char in every 3 lines
# Sum characters (a-z => 1-26 and A-Z => 27-52)

sum = 0

for i in range (0, len(lines), 3):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()
        
    x = ''.join(sorted(set.intersection(set(line1), set(line2), set(line3))))

    if(ord(x) >= 97 and ord(x) <= 122):
        sum += ord(x) - 96
    elif(ord(x) >= 65 and ord(x) <= 90):
        sum += ord(x) - 38
        
print(sum)