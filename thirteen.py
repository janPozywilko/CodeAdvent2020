file = open("thirteen.txt", "r")
data = file.read().split("\n")

time = int(data[0])

bus_lineup_dict = {}

bus_lineup = data[1].split(",")
bus_lineup = [bus for bus in bus_lineup if bus != "x"]

for bus in bus_lineup:
    mod = time % int(bus)
    fixed = time // int(bus)
    bus_lineup_dict[int(bus)] = int(bus) * (fixed + 1)

arr_time = min(bus_lineup_dict.values())

bus_id = [bus for bus in bus_lineup_dict.keys() if bus_lineup_dict[bus] == arr_time]

print(bus_id[0] * (arr_time - time))