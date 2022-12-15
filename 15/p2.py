import re
import sys

file = open('15/in.txt', 'r')
lines = file.readlines()

# Only save row of impossible points, not whole matrix!
# ..####B######################..

sensors = [] # (x, y) sens, 
beacons = set() # (x, y) beacon
dist = [] # dist

# set of points where beacons can't be in row
nobeacons = set()

lineBeaconsOrSensors = 0
lineNoBeaconsLR = [] # (left, right) bounds => count length between bounds
lineLeft = sys.maxsize
lineRight = -sys.maxsize -1

def distance(sens, beacon):
    return abs(sens[0] - beacon[0]) + abs(sens[1] - beacon[1])

def numBlockedOnLineFromSens(line, sens, d):
    x, y = sens
    diff = abs(line - y)
    if(diff > int(d)): return
    num = (d*2+1) - (diff*2)
    # print(num)
    for i in range(num):
        P = ((x-(d-diff))+i, line)
        # print(P)
        if(P in beacons or P in sensors): 
            # print("beacon or sensor", P)
            continue
        nobeacons.add(P)
    return 

def numBlockedOnLineFromSens2(line, sens, d):
    global lineLeft, lineRight, lineBeaconsOrSensors
    x, y = sens
    diff = abs(line - y)
    if(diff > int(d)): return
    num = (d*2+1) - (diff*2)
    # print(num)
    L = (x-(d-diff))
    R = (x+(d-diff))
    
    if(L < lineLeft): lineLeft = L
    if(R > lineRight): lineRight = R
    
def beaconOrSensorOnLine(line):
    global lineBeaconsOrSensors
    for B in beacons:
        if(B[1] == line):
            if(B[0] >= lineLeft and B[0] <= lineRight):
                lineBeaconsOrSensors += 1
    for S in sensors:
        if(S[1] == line):
            if(S[0] >= lineLeft and S[0] <= lineRight):
                lineBeaconsOrSensors += 1
    
    

regs = r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"

for line in lines:
    matches = re.findall(regs, line)
    sensors.append((int(matches[0][0]), int(matches[0][1])))
    B = (int(matches[0][2]), int(matches[0][3]))
    beacons.add(B)
    
    dist.append(distance(sensors[-1], B))
    

    
line = 2000000
# count = 0
for i, d in enumerate(dist):
    # print(sensors[i], beacons[i], d)
    numBlockedOnLineFromSens2(line, sensors[i], d)
    
beaconOrSensorOnLine(line)
    
num = lineRight - lineLeft + 1

print(num - lineBeaconsOrSensors)



# numBlockedOnLineFromSens(8, (8, 7), 9)

# listNoBeacons = list(nobeacons)
# listNoBeacons.sort(key=lambda x: x[0])

# print(listNoBeacons)
# print(len(nobeacons))