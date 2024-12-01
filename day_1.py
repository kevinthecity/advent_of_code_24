import re

def array_distance(array_1, array_2):

	array_1.sort()
	array_2.sort()

	distance = 0

	for i in range(len(array_1)):
		distance += (abs(array_1[i] - array_2[i]))

	return distance

list_a = [3, 4, 2, 1, 3, 3]
list_b = [4, 3, 5, 3, 9, 3]

print(array_distance(list_a, list_b))


list_c = []
list_d = []

f = open("day_1_input.txt", "r")
for line in f:
	pair = re.findall(r"\d+", line)
	list_c.append(int(pair[0]))
	list_d.append(int(pair[1]))
f.close()

print(array_distance(list_c, list_d))