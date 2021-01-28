import math

file = open("five.txt", "r")
data = file.read().splitlines()

test = [
    "FBFBBFFRLR", # Row 44, column 5
    "BFFFBBFRRR", # Row 70, column 7
    "FFFBBBFRRR", # Row 14, column 7
    "BBFFBBFRLL"  # Row 102, column 4
]

ID = []

for row in data:

    lower = 0
    upper = 127
    distance_col = 0

    left = 0
    right = 7
    distance_row = 0

    #Column
    for i in range(0,7):
        if(row[i] == "F"):
            distance_col = upper - lower
            lower = lower
            upper = math.floor(upper - distance_col / 2)
        elif(row[i] == "B"):
            distance_col = upper - lower
            lower = math.ceil(lower + distance_col / 2)
            upper = upper
    
    
    #Row
    for i in range(7,10):
        if(row[i] == "L"):
            distance_row = right - left
            left = left
            right = math.floor(right - distance_row / 2)
        elif(row[i] == "R"):
            distance_row = right - left
            left = math.ceil(left + distance_row / 2)
            right = right
    
    row = min([left, right])
    column = min([lower, upper])
    id = column * 8 + row

    ID.append(id)

submit = max(ID)
ID.sort()



for i in range(45, 954):
    if i not in ID:
        print(i)



# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.