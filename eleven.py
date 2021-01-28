file = open("test.txt", "r")
data = file.read().split("\n")

layout = []

for row in data:

    line = []

    for i in range(0, len(row)):
        line.append(row[i])

    print(line)
    layout.append(line)