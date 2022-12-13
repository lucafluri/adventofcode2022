fileIn = open("13/in2.txt", 'r')
lines = fileIn.read()


lines = lines.split('\n\n')
pairs = []
for pair in lines:
    pair = pair.split('\n')
    pair[0] = eval(pair[0])
    pair[1] = eval(pair[1])
    pairs.append(pair)

# print(pairs)

# Compare func
def compare(l, r):
    print(l, r)
    # Both ints
    if(isinstance(l, int) and isinstance(r, int)):
        if(r < l): return False
        
    
    # Both list
    if(isinstance(l, list) and isinstance(r, list)):
        if(len(l) >= len(r) ):
            for idx, val in enumerate(l):
                compare(val, r[idx])
        else:
            return False
    
    # One of each
    if(isinstance(r, list)):
        return compare([l], r)
    else:
        return compare(l, [r])

for idx, pair in enumerate(pairs):
    print("Pair: ", idx+1, compare(pair[0], pair[1]))
