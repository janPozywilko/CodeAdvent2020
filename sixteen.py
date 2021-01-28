file = open("sixteen.txt", "r")
data = file.read().split(",")

nearby_tickets = data

rules = [   "location: 29-917 or 943-952",
            "station: 50-875 or 884-954",
            "platform: 41-493 or 503-949",
            "track: 50-867 or 875-966",
            "date: 30-655 or 679-956",
            "time: 46-147 or 153-958",
            "location: 50-329 or 344-968",
            "station: 42-614 or 623-949",
            "platform: 35-849 or 860-973",
            "track: 42-202 or 214-959",
            "class: 38-317 or 329-968",
            "duration: 44-530 or 539-953",
            "price: 28-713 or 727-957",
            "route: 30-157 or 179-966",
            "row: 38-114 or 136-969",
            "seat: 45-441 or 465-956",
            "train: 44-799 or 824-951",
            "type: 41-411 or 437-953",
            "wagon: 39-79 or 86-969",
            "zone: 48-306 or 317-974"
        ]

nearby_tickets_test = [
    7,3,47,
    40,4,50,
    55,2,20,
    38,6,12]

valid_tickets = []
not_valid_tickets = []

anserw = 0

for rule in rules:
    rule_row = rule.split(" ")
    rule_row.pop(0)
    rule_row.pop(1)
    line = []
    for elem in rule_row:
            line.append(elem.split("-"))
    for elem in line:
        for i in range(int(elem[0]), int(elem[1]) + 1):
            if i not in valid_tickets:
                valid_tickets.append(int(i))

for ticket in nearby_tickets:
    if int(ticket) not in valid_tickets:
        not_valid_tickets.append(int(ticket))

for ticket in not_valid_tickets:
    anserw += ticket

print(anserw)