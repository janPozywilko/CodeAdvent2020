file = open("three.txt", "r")
data = file.read().splitlines()
data.pop(0)

x_index = 3

width = len(data[0])

tree_counter = 0

solved = []

for row in data:
	if x_index >= width:
		x_index = x_index % width
	
	new_row = ""

	for i in range(len(row)):
		if i == x_index:
			if row[x_index] == "#":
				new_row += "X"
				tree_counter += 1
			else:
				new_row = "0"
		else:
			new_row += row[i]
	x_index += 3

	print(new_row)

