#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(inlist):

    for i in inlist:
        if i == 'term':
            break
        else:
            ##solve
    
    print(result)
#

#Inputting
if __name__ == '__main__':
    start_time = time.time()
    with open('input1.txt', 'r') as input:
        ins = []
        for line in input:
            ins.append(line.strip())
        ins.append('term')
        solve(ins)
    
    print(time.time() - start_time)
#