import functools

fileIn = open("13/in.txt", 'r')
lines = fileIn.read()

lines = lines.split('\n\n')
pairs = []
for pair in lines:
    pair = pair.split('\n')
    pair[0] = eval(pair[0])
    pair[1] = eval(pair[1])
    pairs.append(pair[0])
    pairs.append(pair[1])

# Compare func
def compare(l, r):
    # global res    # Both ints
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

    
    # One of each
    if(isinstance(r, list) and isinstance(l, int)):
        return compare([l], r)
    elif(isinstance(l, list) and isinstance(r, int)):
        return compare(l, [r])
    

pairs.append([[2]])
pairs.append([[6]])
pairs.sort(key=functools.cmp_to_key(compare), reverse=True)
# print(pairs)

print((pairs.index([[2]])+1) * (pairs.index([[6]])+1))