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
    print("BEG ", l, r)
    # Both ints
    if(isinstance(l, int) and isinstance(r, int)):
        print("Both ints")
        if(r < l): return -1
        if(r > l): return 1
        else: return 0
        
    
    # Both list
    if(isinstance(l, list) and isinstance(r, list)):
        print("Both lists")
        if(len(l) == len(r)):
            print("same length")
            for idx in range(len(l)):
                print(idx, l, r)
                ret = compare(l[idx], r[idx])
                print("res", idx, ret)
                if(ret != 0): return ret
                # TODO FIX WHEN RET 0?
                
        elif(len(l) > len(r)):
            print("len left bigger")
            for idx, val in enumerate(r):
                ret = compare(l[idx], r[idx])
                print(ret)
                if(ret != 0): return ret
            return -1
        else: # r bigger than l
            print("len right bigger")
            for idx, val in enumerate(l):
                ret = compare(l[idx], r[idx])
                print(ret)
                if(ret != 0): return ret
            return 1
        # if(len(l) >= len(r) ):
        #     print("same length")
        #     for idx, val in enumerate(r):
        #         # print(val, r[idx]
        #         ret = compare(val, r[idx])
        #         if(ret != 0): return ret
        #         else: continue
        #         # if(not compare(val, r[idx])): return False
        #         # else: continue
        # else:
        #     return -1
    
    # One of each
    if(isinstance(r, list) and not isinstance(l, list)):
        print("One of each")
        return compare([l], r)
    elif(isinstance(l, list) and not isinstance(r, int)):
        return compare(l, [r])
    # return -1
    

c = 2
print(compare(pairs[c-1][0], pairs[c-1][1]))
# for idx, pair in enumerate(pairs):
    # print(pair[0], pair[1])
    # print("Result: ", compare(pair[0], pair[1]))
