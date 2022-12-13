fileIn = open("13/in.txt", 'r')
lines = fileIn.read()

lines = lines.split('\n\n')
pairs = []
for pair in lines:
    pair = pair.split('\n')
    pair[0] = eval(pair[0])
    pair[1] = eval(pair[1])
    pairs.append(pair)

# Compare func
def compare(l, r):
    if(isinstance(l, int) and isinstance(r, int)):
        if(r < l): 
            return -1
        elif(r > l): 
            return 1
        else: 
            return 0
        
    
    # Both list
    if(isinstance(l, list) and isinstance(r, list)):
        if(len(l) == len(r)):
            for idx in range(len(l)):
                ret = compare(l[idx], r[idx])
                if(ret != 0 and ret != None): return ret

                
        elif(len(l) > len(r)):
            for idx in range(len(r)):
                ret = compare(l[idx], r[idx])
                if(ret != 0 and ret != None): return ret
            return -1
        else: # r bigger than l
            for idx in range(len(l)):
                ret = compare(l[idx], r[idx])
                
                if(ret != 0 and ret != None): return ret
            return 1

    
    if(isinstance(r, list) and isinstance(l, int)):
        return compare([l], r)
    elif(isinstance(l, list) and isinstance(r, int)):
        return compare(l, [r])



count = 0;
for idx, pair in enumerate(pairs):
    comp = compare(pair[0], pair[1])
    
    if(comp == 1): count += idx+1

print(count)