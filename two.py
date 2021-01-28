passwords = []

with open('two.txt') as two:
	for line in two:
		passwords.append(line)


valid_passwords = []

for element in passwords:	

	limits, letter, password = element.split(" ")

	lower_limit, upper_limit = limits.split("-")

	key_letter = letter.split(":")[0]

	counter = 0

	for letter in password:

		if(letter == key_letter):
			counter += 1

	
	if(counter >= int(lower_limit) and counter <= int(upper_limit)):
		valid_passwords.append(password)


print(len(passwords), "******")
print(len(valid_passwords))
