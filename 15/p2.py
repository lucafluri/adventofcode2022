import re
import sys

file = open('15/in.txt', 'r')
lines = file.readlines()

# Only save row of impossible points, not whole matrix!
# ..####B######################..

MAXXY = 4000000

sensors = [] # (x, y) sens, 
beacons = set() # (x, y) beacon
dist = [] # dist

# set of points where beacons can't be in row
# nobeacons = set()


segments = [] # (left, right) bounds from 0 to 4000000

lineBeaconsOrSensors = 0
lineNoBeaconsLR = [] # (left, right) bounds => count length between bounds
lineLeft = sys.maxsize
lineRight = -sys.maxsize -1

def distance(sens, beacon):
    return abs(sens[0] - beacon[0]) + abs(sens[1] - beacon[1])

def numBlockedOnLineFromSens2(line, sens, d):
    global lineLeft, lineRight, lineBeaconsOrSensors, MAXXY
    x, y = sens
    # if(x < 0 or y > 4000000): return
    diff = abs(line - y)
    if(diff > int(d)): return
    num = (d*2+1) - (diff*2)
    # print(num)
    L = (x-(d-diff))
    R = (x+(d-diff))
    L = max(L, 0)
    R = min(R, MAXXY)
    
    segments.append((L, R))
        
    
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

def combineSegments():
    global segments
    segments.sort(key=lambda x: x[0])
    i = 0
    while(i < len(segments)-1):
        if(segments[i][1] >= segments[i+1][0]):
            segments[i] = (segments[i][0], max(segments[i][1], segments[i+1][1]))
            segments.pop(i+1)
        else:
            i += 1
            

def printTuningFrequency(x, y):
    print(x*4000000 + y)
    

regs = r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"

for line in lines:
    matches = re.findall(regs, line)
    sensors.append((int(matches[0][0]), int(matches[0][1])))
    B = (int(matches[0][2]), int(matches[0][3]))
    beacons.add(B)
    
    dist.append(distance(sensors[-1], B))
    

    
# Runtime approx 75 seconds for 4000000 lines
for X in range(MAXXY): 
    lineLeft = sys.maxsize
    lineRight = -sys.maxsize -1
    segments = []
    for i, d in enumerate(dist):
        # print(sensors[i], beacons[i], d)
        numBlockedOnLineFromSens2(X, sensors[i], d)
    combineSegments()
    # print(segments)
    if(len(segments) > 1 and segments[0][1] != segments[1][0]-1): 
        XCoord = segments[0][1] + 1
        print("GAP FOUND AT LINE", XCoord, X)
        printTuningFrequency(XCoord, X)
