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
            index = 4
            while index < len(i) - 4:
                chars = [x for x in i[index:index+4]]
                dict = {}
                for char in chars:
                    if char in dict:
                        break
                    else:
                        dict[char] = True
                
                if len(dict.keys()) == 4:
                    result = index + 4
                    print(result)
                    break
                index += 1
    
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