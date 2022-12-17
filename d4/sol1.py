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
            ##solve
            i = i.replace(",", "-")
            
            elfs_ranges = [int(x) for x in i.split("-")]
            ldiff = elfs_ranges[0] - elfs_ranges[2]
            ldiffsign = 0 if ldiff == 0 else ldiff/abs(ldiff)

            rdiff = elfs_ranges[1] - elfs_ranges[3]
            rdiffsign = 0 if rdiff == 0 else rdiff/abs(rdiff)
            if ldiffsign == -1*rdiffsign or ldiffsign == 0 or rdiffsign == 0:
                total += 1
            
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