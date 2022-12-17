#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(inlist):

    trigroup = []
    total = 0

    for i in inlist:
        trigroup.append(i)
        if len(trigroup) == 3:
            
            #Idea is to iteratively find set(Sack1) AND set(Sack2) AND set(Sack3)
            #Hashmap speeds up the and process
            all_dict = {}
            init = True
            for sack in trigroup:
                
                #Generate set: Find all unique chars in current sack
                line_dict = {}
                for char in sack:
                    line_dict[char] = 1

                    #If nothing in total sack then add it to there also
                    if init == True:
                        all_dict[char] = 1
                
                if init == True:
                    init = False
                
                #AND step: Keep only common chars between total sack and current sack
                new_total = {}
                for key in all_dict:
                    if key in line_dict:
                        new_total[key] = 1
                
                all_dict = dict(new_total)

                #Then repeats for next sacks
            
            #Calculate score
            for char in all_dict:
                score = ord(char)
                if score < 97:
                    #uppercase letters
                    score += - 65 + 27 
                    total += score
                else:
                    #lower case letters
                    score += - 96
                    total += score            
            
            #reset trigroup
            trigroup = []

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