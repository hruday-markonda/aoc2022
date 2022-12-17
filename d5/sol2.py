#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(inlist):

    #Find line with the box numbers
    line_num = 0
    for i in inlist:
        if i.strip() == "":
            break
        else:
            line_num += 1
    
    # Get location index and prepare the stacks
    stacks = {}
    index = 0
    indexes = []
    for char in inlist[line_num - 1]:
        if char.isnumeric():
            indexes.append(index)
            key = int((index - 1)/4) + 1
            stacks[key] = []
        index += 1
    
    # add items to stack
    cur_line = 0
    while cur_line < line_num - 1:
        i = inlist[cur_line]
        if i == "":
            break
        
        else:
            for index in indexes:
                if i[index].strip() != "":
                    key = int((index - 1)/4) + 1
                    stacks[key].insert(0, i[index])
        
        cur_line += 1
    
    cur_line = line_num + 1

    while cur_line < len(inlist) - 1:
        raw_cmd = inlist[cur_line].replace("move ", "").replace(" from ", ",").replace(" to ", ",")
        cmd = [int(x) for x in raw_cmd.split(",")]
        
        iter = 0
        init_len = len(stacks[cmd[2]])
        while iter < cmd[0]:
            stacks[cmd[2]].insert(init_len, stacks[cmd[1]].pop())
            iter += 1

        cur_line += 1
    
    message = "".join([stacks[x][-1] for x in stacks])
    print(message)
    
#

#Inputting
if __name__ == '__main__':
    start_time = time.time()
    with open('input2.txt', 'r') as input:
        ins = []
        for line in input:
            ins.append(line)
        ins.append('term')
        solve(ins)
    
    print(time.time() - start_time)
#