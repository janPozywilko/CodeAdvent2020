passwords = []

with open('two.txt') as two:
	for line in two:
		passwords.append(line)


valid_passwords = []

for element in passwords:	

	indexes, letter, password = element.split(" ")

	index_one, index_two = indexes.split("-")

	key_letter = letter.split(":")[0]

	if((password[int(index_one) - 1] == key_letter) ^ (password[int(index_two) - 1] == key_letter)):
		valid_passwords.append(password)

print(len(valid_passwords))
