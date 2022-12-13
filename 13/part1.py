fileIn = open("13/in.txt", 'r')
lines = fileIn.read()


lines = lines.split('\n\n')
pairs = []
for pair in lines:
    pair = pair.split('\n')
    pair[0] = eval(pair[0])
    pair[1] = eval(pair[1])
    pairs.append(pair)

# print(pairs)

# res = 0

# Compare func
def compare(l, r):
    # global res
    # if(res != 0 and res != None): return res
    # print("BEG ", l, r)
    # Both ints
    if(isinstance(l, int) and isinstance(r, int)):
        # print("Both ints")
        if(r < l): 
            # print("r < l")
            return -1
        elif(r > l): 
            # print("r > l")
            return 1
        else: 
            # print("r == l")
            return 0
        
    
    # Both list
    if(isinstance(l, list) and isinstance(r, list)):
        # print("Both lists")
        if(len(l) == len(r)):
            # print("same length")
            for idx in range(len(l)):
                # if(res): return res
                ret = compare(l[idx], r[idx])
                if(ret != 0 and ret != None): return ret

                
        elif(len(l) > len(r)):
            # print("len left bigger")
            for idx in range(len(r)):
                # if(res): return res
                ret = compare(l[idx], r[idx])
                # print("ret", ret)
                # return ret
                if(ret != 0 and ret != None): return ret
                # print("wtf")
                # print("ret", ret, res)
                # if(ret != 0): return ret
            return -1
        else: # r bigger than l
            # print("len right bigger")
            for idx in range(len(l)):
                # if(res): return res
                ret = compare(l[idx], r[idx])
                
                if(ret != 0 and ret != None): return ret
                # print("ret", ret, res)
                # if(ret != 0): return ret
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
    if(isinstance(r, list) and isinstance(l, int)):
        # print("One of each")
        return compare([l], r)
    elif(isinstance(l, list) and isinstance(r, int)):
        return compare(l, [r])
    # return -1
    

# c = 3
# print(compare(pairs[c-1][0], pairs[c-1][1]))
# print(res)


count = 0;
for idx, pair in enumerate(pairs):
    print(pair[0], pair[1])
    comp = compare(pair[0], pair[1])
    print(comp)
    # print("Result: ", res)
    
    if(comp == 1): count += idx+1
    # res = 0

print(count)