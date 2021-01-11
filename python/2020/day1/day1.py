
from itertools import combinations
with open("./input.txt") as file:
    data = [int(line) for line in file]
    #print(data)

# quiz-1
for combo in combinations(data, 2):
    if combo[0] + combo[1] == 2020:
        print("numbers: {},{}".format(combo[0],combo[1]))
        mult1 = combo[0]*combo[1]
        print(mult1)

        
# quiz-2
for combo in combinations(data, 3):
    if combo[0] + combo[1] + combo[2] == 2020:
        print("numbers: {},{},{}".format(combo[0],combo[1],combo[2]))
        mult2 = combo[0]*combo[1]*combo[2]
        print(mult2)




              
              

