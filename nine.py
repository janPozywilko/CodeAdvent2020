file = open("nine.txt", "r+")

data = file.read().splitlines()

preamble = []
preamble_size = 25
counter = 0
condition = True
anserw = 0

while counter != preamble_size:
    preamble.append(data[0])
    data.pop(0)
    counter += 1



while condition:

    current = data[0]
    test_list = []

    for element1 in preamble:
        for element2 in preamble:
            sum = int(element1) + int(element2)
            test_list.append(sum)

    test_list = list(dict.fromkeys(test_list))

    if(int(current) not in test_list):
        condition = False
        anserw = current
            
    preamble.pop(0)
    preamble.append(data[0])
    data.pop(0)

print("anserw: ", anserw)