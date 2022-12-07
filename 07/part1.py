file = open('in.txt', 'r')
lines = file.readlines()

# Calculate size for each directory recursively
# Print sum of all directories <= 100'000
# Files can be counted multiple times (nested directories)

# Build dir tree while iterating over input
# Add size of each file to its parent directory
# Keep list of all directory nodes with size <= 100'000

class Node:
    def __init__(self, name, size=0):
        self.name: str = name
        self.size: int = size
        self.parent: DirNode = None

    def get_size(self):
        return self.size
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_parent(self):
        return self.parent
    
    def __str__(self):
        return self.name + ' ' + str(self.size)
    
class DirNode(Node):
    def __init__(self, size=0):
        super().__init__(size)
        self.children = []
    
    def get_children(self):
        return self.children
    
    def add_child(self, child):
        child.set_parent(self)
        self.children.append(child)
    
    def __str__(self):
        return 'DIR ' + super().__str__()
        
        
        
class FileNode(Node):
    def __str__(self):
        return 'FILE ' + super().__str__()





def addDir(name):
    global currentDir
    currentDir.add_child(DirNode(name))

def addFile(name, size):
    global currentDir
    currentDir.add_child(FileNode(name, size))
    increaseDirSize(size)
    
def increaseDirSize(size):
    global currentDir
    currentDir.size += size
    # Increase size of all parent directories
    n = currentDir.get_parent()
    while(n != None):
        n.size += size
        n = n.get_parent()
    # currentDir.size += size


def handleCommand(line):
    global currentDir
    line.strip()
    line = line.split()
    
    if(line[1] == 'cd'):
        if(line[2] == '..'):
            currentDir = currentDir.get_parent()
        elif(line[2] == '/'):
            currentDir = root
        else:
            search = list(filter(lambda x: isinstance(x, DirNode) and x.name == line[2], currentDir.get_children()))
            currentDir = search[0] 

    elif(line[1] == 'ls'):
        pass
    

# Print tree
def printTree(node, depth):
    print('-|' * depth + str(node))
    for n in node.get_children():
        if isinstance(n, DirNode):
            printTree(n, depth + 1)
            
            

def parseTree(node):
    global dirNodes
    if isinstance(node, DirNode):
        if(node.get_size() <= 100000):
            dirNodes.append(node)
        
        for n in node.get_children():
            parseTree(n)
            


# ========================================================
# =======================MAIN=============================
# ========================================================



# Keep track
root: DirNode = DirNode('/')
currentDir: Node = root

# List of dir nodes to filter later
dirNodes = []

# Iterate over input
for line in lines:
    # Options: $ cd X, $ ls, dir X, 1234 X
    
    if(line.startswith('$')):
        handleCommand(line)
        continue
    
    line = line.strip()
    line = line.split(' ')
    if(line[0] == 'dir'):
        addDir(line[1])
    else:
        addFile(line[1], int(line[0]))
        
# printTree(root, 0)

# nodes = list(filter(lambda x: x.get_size() <= 100000, dirNodes))
sum = 0

parseTree(root)
for n in dirNodes:
    # print(n)
    sum += n.get_size()

print(sum)