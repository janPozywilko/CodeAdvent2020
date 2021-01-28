from collections import Counter

file = open("six.txt", "r")

data = file.read().split("\n\n")

alphabet = "qwertyuiopasdfghjklzxcvbnm"

final = []

sum = 0

for row in data:
    elements = row.split("\n")
    line = []
    row_count = 0
    for element in elements:
        for i in range(len(element)):
            line.append(element[i])
    counter = Counter(line)
    for item in counter:
        if counter[item] == len(elements):
            row_count += 1
    print(elements)
    print(row_count)
    sum += row_count
print(sum)