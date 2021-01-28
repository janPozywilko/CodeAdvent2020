file = open("ten.txt", "r")
data = file.read().split("\n")

joltages = []
ones = []
threes = []

for row in data:
    joltages.append(int(row))

joltages.append(0)
joltages.append(max(joltages) + 3)

joltages.sort()


for i in range(0, len(joltages) - 1):
    difference = joltages[i + 1] - joltages[i]

    if(difference == 1):
        ones.append(1)
    elif(difference == 3):
        threes.append(3)


print("Anserw: ", len(ones) * len(threes))