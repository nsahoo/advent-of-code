
from itertools import combinations
with open("./input.txt") as file:
    data = [int(line) for line in file]
    #print(data)

##########    
# quiz-1
##########
# method-1
for combo in combinations(data, 2):
    if combo[0] + combo[1] == 2020:
        print("numbers: {},{}".format(combo[0],combo[1]))
        mult1 = combo[0]*combo[1]
        print(mult1)

        
# method-2
for i in data:
    for j in data:
        if i+j == 2020:
            print(i*j)

            
# method-3 (one-liner)
part1 = max(i*j if i + j == 2020 else 0 for i in data for j in data)
print(part1)        

##########
# quiz-2
##########
#method-1
for combo in combinations(data, 3):
    if combo[0] + combo[1] + combo[2] == 2020:
        print("numbers: {},{},{}".format(combo[0],combo[1],combo[2]))
        mult2 = combo[0]*combo[1]*combo[2]
        print(mult2)

# method-2
for i in data:
    for j in data:
        for k in data:
            if i+j+k == 2020:
                print(i*j*k)
            
# method-3 (one-liner)
part2 = max(i*j*k if i + j + k == 2020 else 0 for i in data for j in data for k in data)
print(part2)


              
              


