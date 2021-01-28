file = open("twelve.txt", "r")

data = file.read().split("\n")

directions = ["N", "E", "S", "W"] # List of possible directions

curr_direction = 1 # Index of current direction


x_pos = 0
y_pos = 0


for row in data:
    
    rule = row[0]
    value = int(row[1:])

    if(rule == "L"):
        if(value == 90):
            curr_direction = (curr_direction - 1) % 4
        elif(value == 180):
            curr_direction = (curr_direction - 2) % 4
        elif(value == 270):
            curr_direction = (curr_direction - 3) % 4
    elif(rule == "R"):
        if(value == 90):
            curr_direction = (curr_direction + 1) % 4
        elif(value == 180):
            curr_direction = (curr_direction + 2) % 4
        elif(value == 270):
            curr_direction = (curr_direction + 3) % 4
    elif(rule == "N"):
        y_pos += value
    elif(rule == "S"):
        y_pos -= value
    elif(rule == "E"):
        x_pos += value
    elif(rule == "W"):
        x_pos -= value
    elif(rule == "F"):
        if(curr_direction == 0):
            y_pos += value
        elif(curr_direction == 1):
            x_pos += value
        elif(curr_direction == 2):
            y_pos -= value
        elif(curr_direction == 3):
            x_pos -= value

print("Anserw: ", abs(x_pos) + abs(y_pos))