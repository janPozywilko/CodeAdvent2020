file = open("eight.txt", "r")
data = file.read().splitlines()

indexes = []
index = 0
acc = 0

instructions = [row.split(" ") for row in data]

while index not in indexes:
    instruction = instructions[index]

    if(instruction[0] == "nop"):
        indexes.append(index)
        index += 1
    elif(instruction[0] == "acc"):
        acc += int(instruction[1])
        indexes.append(index)
        index += 1
    elif(instruction[0] == "jmp"):
        indexes.append(index)
        index += int(instruction[1])
        

print(acc)