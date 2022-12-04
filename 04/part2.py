file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0

for line in lines:
    seqs =  line.split(',')
    s1 = seqs[0].strip()
    s2 = seqs[1].strip()
    
    a, b = s1.split('-')
    c, d = s2.split('-')
    
    # COnvert to int!!
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    
    # Case 1: a >= c and b <= d
    # Case 2: c >= a and d <= b
    
    # A-B, C-D
    if(a >= c and b <= d): # S1 in S2
        sum+=1
    elif(a <= c and b >= d): # S2 in S1
        sum+=1

    # Find overlaps
    elif(a <= c and b >= c and b <= d): # S1 overlaps S2
        sum+=1
    elif(a >= c and a <= d and b >= d): # S2 overlaps S1
        sum+=1
    
print(sum)
    
    