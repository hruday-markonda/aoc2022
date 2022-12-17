#Imports
import time
#

#Problem Functions
def work():
    pass

def solve(inlist):
    win = ["B", "C", "A"]
    lose = ["C", "A", "B"]
    scores = {"A": 1, "B": 2, "C": 3}
    total = 0

    for i in inlist:
        if i == 'term':
            break
        else:
            condition = i[2]
            bot = i[0]

            index = scores[bot] - 1

            if condition == "X":
                index = scores[bot] - 1
                loser = lose[index]
                loser_score = scores[loser]
                total += loser_score

            elif condition == "Y":
                draw_score = scores[bot]
                total += draw_score + 3

            elif condition == "Z":                
                index = scores[bot] - 1
                winner = win[index]
                winner_score = scores[winner]
                total += winner_score + 6

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