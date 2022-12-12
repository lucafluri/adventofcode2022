import re

fileIn = open('11/in.txt', 'r')
file = fileIn.read()

class Monkey:
    def __init__(self, id, items, op, val, div, tMonkey, fMonkey):
        self.id = int(id)
        self.items = items
        self.op = op # +, *
        self.val = val # number, old
        self.div = int(div)
        self.tMonkey = int(tMonkey)  
        self.fMonkey = int(fMonkey)
        self.inspectionCount = 0
    
    def __str__(self):
        return f"Monkey {self.id}: {self.items}, {self.op}, {self.val}, {self.div}, {self.tMonkey}, {self.fMonkey}, {self.inspectionCount}"
    
    def __lt__(self, other):
        return self.inspectionCount < other.inspectionCount
    
        
# Monkey list:
monkeys = []

regString = r"Monkey (\d):\s*Starting items: ((?:\d+,?[^\S\r\n]?)+)\s+.*old (.) (\w+)?\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)"
res = re.findall(regString, file)

# print(res)
for m in res:
    monkeys.append(Monkey(m[0], m[1].split(','), m[2], m[3], m[4], m[5], m[6]))
    monkeys[-1].items = [int(i) for i in monkeys[-1].items]
    # print(monkeys[-1])
    

# Worry levels get divided by three after before tests
# Rounds
for i in range(10000):
    for m in monkeys:
        # print(m)
        for item in m.items:
            m.inspectionCount += 1
            old = item
            if(m.op == '*'):
                if(m.val == 'old'):
                    item = old * old
                else: item = old * int(m.val)
            elif(m.op == "+"):
                if(m.val == 'old'):
                    item = old + old
                else: item = old + int(m.val)
                
            # op = f"{item} {m.op} {m.val}"
            # print(op)
            # item = eval(op)
            # item = int(item / 3)
            item = item % (2*3*5*7*11*13*17*19)
            # print(m)
            if(item % m.div == 0):
                monkeys[m.tMonkey].items.append(item)
            else: 
                monkeys[m.fMonkey].items.append(item)
            m.items = m.items[1:]

for m in monkeys:
    print(m)
    
# sort monkeys after inspectioncount:
monkeys.sort(reverse=True)
print(monkeys[0].inspectionCount * monkeys[1].inspectionCount)

