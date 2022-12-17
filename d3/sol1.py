#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(inlist):

    total = 0
    for i in inlist:
        if i == 'term':
            break
        else:
            hashmap = {}
            index = 0

            #load into hashmap each char in compart 1 if not exists
            while index < len(i)/2:
                if i[index] not in hashmap:
                    hashmap[i[index]] = 1
                index += 1
        
            #loop over second half and add to total
            while index < len(i):
                if i[index] in hashmap:
                    char = i[index]
                    score = ord(char)
                    if score < 97:
                        #uppercase letters
                        score += - 65 + 27 
                        total += score
                    else:
                        #lower case letters
                        score += - 96
                        total += score
                    print(str(i[index]) + str(score))
                    break
                index += 1
    
    print(total)
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