import re

file = open('15/in.txt', 'r')
lines = file.readlines()

sensors = [] # (x, y) sens, 
beacons = [] # (x, y) beacon
dist = [] # dist

# set of points where beacons can't be
nobeacons = set()

def distance(sens, beacon):
    return abs(sens[0] - beacon[0]) + abs(sens[1] - beacon[1])

regs = r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"

for line in lines:
    matches = re.findall(regs, line)
    sensors.append((int(matches[0][0]), int(matches[0][1])))
    beacons.append((int(matches[0][2]), int(matches[0][3])))
    dist.append(distance(sensors[-1], beacons[-1]))
    
    # Add all points between sensor and hamming distance to nobeacons
    for x in range(-dist[-1], dist[-1] + 1):
        for y in range(-dist[-1], dist[-1] + 1):
            P = (sensors[-1][0] + x, sensors[-1][1] + y)
            if distance(sensors[-1], P) <= dist[-1]:
                if(P not in beacons and P not in sensors):
                    nobeacons.add(P)
                # nobeacons.add((sensors[-1][0] + x, sensors[-1][1] + y))
    
# print(dist)
listNoBeacons = list(nobeacons)
listNoBeacons.sort(key=lambda x: x[1])
# print(listNoBeacons)
# Filter out beacon and sensor points
print(len(list(filter(lambda x: x[1] == 10, listNoBeacons))))
