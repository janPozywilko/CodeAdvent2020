import math

file = open("five.txt", "r")
data = file.read().splitlines()

test = [
    "FBFBBFFRLR", # Row 44, column 5
    "BFFFBBFRRR", # Row 70, column 7
    "FFFBBBFRRR", # Row 14, column 7
    "BBFFBBFRLL"  # Row 102, column 4
]


for row in test:

    lower = 0 #lower limit
    upper = 127 #upper limit
    distance_column = 0 #distance between upper and lower limit

    left = 0
    right = 7
    distance_row = 0

    #Column
    for i in range(0,7):
        if(row[i] == "F"):
            distance_column = upper - lower
            lower = lower
            upper = math.floor(upper - (distance_column / 2))
        elif(row[i] == "B"):
            distance = upper - lower
            lower = math.ceil(lower + (distance_column / 2))
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

    print("Your column is: ", column, ". Your row is: ", row)



# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.