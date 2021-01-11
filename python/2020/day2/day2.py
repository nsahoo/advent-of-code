

with open("./input.txt") as file:
    data = [line for line in file]
    #print(data)


# quiz-1

valid = 0
for entry in data:
    entry = entry.split()
    #print(entry)
    numbers = entry[0].split(sep="-")
    #print(numbers)
    minimum = int(numbers[0])
    maximum = int(numbers[1])
    #print(minimum,maximum)

    letter = entry[1][0]
    password = entry[2]
    #print(letter,password)

    if minimum <= password.count(letter) <= maximum:
        valid += 1

print(valid)        


# quiz-2

valid2 = 0
for entry in data:
    entry = entry.split()
    numbers = entry[0].split(sep="-")
    pos1 = int(numbers[0])-1
    pos2 = int(numbers[1])-1
    #print(pos1, pos2)

    letter = entry[1][0]
    password = entry[2]

    first  = (password[pos1] == letter)
    second = (password[pos2] == letter)
    combo = first ^ second     # XOR
    #print(first,second,combo)
    
    if combo:
        valid2 += 1
        
print(valid2)    
