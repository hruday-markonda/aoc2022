#Imports
import time
#

#Problem Functions
class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return str(self.start) + " " + str(self.end)

def solve(inlist):

    total = 0
    for i in inlist:
        if i == 'term':
            break
        else:
            ##solve
            i = i.replace(",", "-")
            elfs_ranges = [int(x) for x in i.split("-")]
            intervals = [interval(elfs_ranges[0], elfs_ranges[1]), interval(elfs_ranges[2], elfs_ranges[3])]
            intervals.sort(key = lambda x: x.start, reverse = False)
            
            interval1 = intervals[0]
            interval2 = intervals[1]

            if interval2.start <= interval1.end:
                total += 1
            
            
    print(total)
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