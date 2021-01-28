file = open("fifteen.txt", "r")
data = file.read().split("\n")

data_set = data[0].split(",")
data_set = [int(item) for item in data_set]

array = data_set
index = len(array) - 1
new_element = 0

while len(array) != 2020:
    last_spoken = array[-1]
    indices = [i for i, x in enumerate(array) if x == last_spoken]
    if(len(indices) == 1):
        array.append(0)
    else:
        array.append(indices[-1] - indices[-2])

print(array[-1])
