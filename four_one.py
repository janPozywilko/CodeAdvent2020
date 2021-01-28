file = open("four.txt", "r")
data = file.read().split("\n\n")

form = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]


valid_counter = 0

for row in data:
    
    formated = row.split("\n")
    elements = " ".join(formated).split(" ")

    line = []

    for element in elements:
        category = element.split(":")[0]
        line.append(category)

    check = all(item in  line for item in form)
    
    if check:
        valid_counter += 1


print(valid_counter)


#it's splitting on every new empty line but it fails to produce correct anserw when there the new line is not empty

