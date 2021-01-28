import numpy as np

array = np.loadtxt('one.txt', delimiter = "\n")

for i in array:
	for j in array:
		for z in array:	
			sum = i + j + z
			if(sum == 2020): print(i , j, z)


