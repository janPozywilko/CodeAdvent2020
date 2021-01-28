file = open("six.txt", "r")

data = file.read().split("\n\n")

count = 0

for row in data:
    elements = "".join(row.split("\n"))
    elements_arr = [char for char in elements]
    group = list(dict.fromkeys(elements_arr))
    count += len(group)

print("Count: ", count)    