#Imports
import time
#

# Global Vars
topthree = []
count = 0
#

#Problem Functions
def work():
    pass

def solve(inlist):
    global max
    global count
    
    for _in in inlist:
        if _in == 'term' or _in.isnumeric() == False:
            if len(topthree) < 3:
                topthree.append(count)
                topthree.sort()
            else:
                for i in range(0,3):
                    if count > topthree[i]:
                        topthree[i] = count
                        topthree.sort()
                        break
            count = 0

        elif _in.isnumeric() == True:
            count += int(_in)
        
#

#Inputting
if __name__ == '__main__':
    start_time = time.time()
    with open('input.txt', 'r') as input:
        ins = []
        for line in input:
            ins.append(line.strip())
        ins.append('term')
        solve(ins)
    print(sum(topthree))
    print(time.time() - start_time)

#