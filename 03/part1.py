file1 = open('input.txt', 'r')
lines = file1.readlines()

# Find common char in both halfs of the string
# Sum characters (a-z => 1-26 and A-Z => 27-52)

sum = 0

for line in lines:
    line = line.strip()
    size = int(len(line) / 2) # Per Compartment
    
    s1 = line[:size]
    s2 = line[size:]
    
    x = ''.join(sorted(set.intersection(set(s1), set(s2))))
    
    if(ord(x) >= 97 and ord(x) <= 122):
        sum += ord(x) - 96
    elif(ord(x) >= 65 and ord(x) <= 90):
        sum += ord(x) - 38
        
print(sum)