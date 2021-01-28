file = open("seven.txt", "r")
data = file.read().splitlines()

colors = {}
counter = 0

for row in data:
    removed = row.replace("bags contain", "").replace("bags", "").replace("bag", "").replace(",", "").replace(".", "")
    removed = removed.split(" ")
    removed = [item for item in removed if not(item.isdigit()) and item != ""]
    
    line = []

    for i in range(0, int(len(removed) / 2)):
        color = ""
        color += removed[2 * i]
        color += removed[2 * i + 1]
        if color != "noother": line.append(color)

    key = line[0]
    line.pop(0)
    
    colors[key] = line 

for key in colors:
    line = []
    for color in colors[key]:
        if color != "shinygold": 
            for element in colors[color]: 
                line.append(element)
        else: line.append(color)
    colors[key] = line

for key in colors:
    if("shinygold" in colors[key]): counter += 1

print(counter)        



