#Imports
import time
#

#Problem Functions
class node:
    
    name:str
    parent:'node'
    childs:'list'
    _type:str
    size:int 

    def __init__(self, parent, name, _type, size):
        self.parent = parent
        self.name = name
        self.size = size
        self._type = _type
        self.childs = []
    
    def update_weight(self):
        self.size = 0
        for child in self.childs:
            self.size += child.size
    
    def add_child(self, child):
        self.childs.append(child)
        self.update_weight()
    
    def __repr__(self):
        return f"{self._type} : {self.name} : {self.size}"

class tree:

    root:'node'
    current_node:'node'

    def __init__(self):
        self.root = node(None, '/', 'dir', 0)
        self.current_node = self.root
    
    def add_child(self, child):
        self.current_node.add_child(child)
    
    def set_root(self):
        self.current_node = self.root
    
    def update_weight(self):
        cur_node = self.current_node
        while cur_node != None:
            cur_node.update_weight()
            cur_node = cur_node.parent

    def switch_dir(self, dir_name):
        for child in self.current_node.childs:
            if child.name == dir_name and child._type == 'dir':
                self.current_node = child
                return

def solve(inlist):

    command = True
    dir_tree = tree()

    for i in inlist:
        if i == 'term':
            break
        else:
            ##solve
            cmd = i[0:4]

            if cmd == "$ ls" and command == True:
                command = False
            
            elif i == "$ cd ..":
                command = True
                dir_tree.current_node = dir_tree.current_node.parent
                    
            elif cmd == "$ cd":
                command = True
                dir = i.split()[2]
                if dir == "/":
                    dir_tree.set_root()
                else:
                    dir_tree.switch_dir(dir)

            elif command == False:
                
                child = i.split()
                new_child = None
                if child[0] == "dir":
                    new_child = node(dir_tree.current_node, child[1], "dir", 0)
                
                else:
                    new_child = node(dir_tree.current_node, child[1], "file", int(child[0]))
                dir_tree.add_child(new_child)
                dir_tree.update_weight()   

    max_size = dir_tree.root.size
    required = 30000000 - (70000000 - dir_tree.root.size)

    def find_size(cur_dir):
        nonlocal max_size
        nonlocal required
        #print(cur_dir.size)
        if cur_dir.size <= max_size and cur_dir.size > required:
            max_size = cur_dir.size

        for child in cur_dir.childs:            
            if child._type == "dir":
                find_size(child)

    find_size(dir_tree.root)
    print(max_size)
#

#Inputting
if __name__ == '__main__':
    start_time = time.time()
    with open('input2.txt', 'r') as input:
        ins = []
        for line in input:
            ins.append(line.strip())
        ins.append('term')
        solve(ins)
    
    print(time.time() - start_time)
#