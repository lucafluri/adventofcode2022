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
        print("Both ints")
        if(r < l): return False
        if(r > l): return True
        
    
    # Both list
    if(isinstance(l, list) and isinstance(r, list)):
        print("Both lists")
        if(len(l) >= len(r) ):
            print("same length")
            for idx, val in enumerate(l):
                # print(val, r[idx]
                ret = compare(val, r[idx])
                if(ret): return True
                # if(not compare(val, r[idx])): return False
                # else: continue
        else:
            return False
    
    # One of each
    if(isinstance(r, list)):
        print("One of each")
        return compare([l], r)
    elif(isinstance(l, list)):
        return compare(l, [r])
    return False
    

c = 1
print(compare(pairs[c][0], pairs[c][1]))
# for idx, pair in enumerate(pairs):
    # print(pair[0], pair[1])
    # print("Result: ", compare(pair[0], pair[1]))
