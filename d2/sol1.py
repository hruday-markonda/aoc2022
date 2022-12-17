#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(inlist):
    same = ["A", "B", "C"]
    wins = ["C", "A", "B"]
    scores = {"X":1, "Y":2, "Z":3}
    total = 0

    for i in inlist:
        if i == 'term':
            break
        else:
            mymove = str(i[2])
            bot = str(i[0])
            index = scores[mymove] - 1
            total += index + 1

            if wins[index] == bot:
                total += 6 
            elif same[index] == bot:
                total += 3
    
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