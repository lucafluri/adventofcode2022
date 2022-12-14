file = open('14/in.txt', 'r')
lines = file.readlines()

rock = set()
sand = set()

for line in lines:
    line = line.strip().split(' -> ')
    p0 = None
    for point in line:
        p = (int(point.split(',')[0]), int(point.split(',')[1]))
        if(p0 == None): 
            p0 = p
            continue
        
        # print(p0, p)
        
        if(p0[0] == p[0]):
            
            for i in range(min(p0[1], p[1]), max(p0[1], p[1])+1):
                p1 = (p0[0], i)
                # if(p1 not in rock): rock.append(p1)
                rock.add(p1)
        elif(p0[1] == p[1]):
            for i in range(min(p0[0], p[0]), max(p0[0], p[0])+1):
                p1 = (i, p0[1])
                # if(p1 not in rock): rock.append(p1)
                rock.add(p1)
        p0 = p

rockList = list(rock)
rockList.sort(key=lambda x: x[1])
lowestPoint = rockList[-1][1]
print("Lowest Point", lowestPoint)

def isFree(P):
    x, y = P
    return not (x, y) in rock and not(x, y) in sand

def fallsIntoAbyss(P):
    x, y = P
    return y > lowestPoint



S = (500, 0)
while(not fallsIntoAbyss(S)):
    SS = (S[0], S[1]+1)
    SW = (S[0]-1, S[1]+1)
    SE = (S[0]+1, S[1]+1)
    
    if(isFree(SS)):
        S = SS
    elif(isFree(SW)):
        S = SW
    elif(isFree(SE)):
        S = SE
    else:
        sand.add(S)
        S = (500, 0)

print(len(sand))
        
