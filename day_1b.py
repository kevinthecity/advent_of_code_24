import re


def similarity_score(array_1, array_2):

    score = 0

    for i in range(len(array_1)):
        score += (count_instances(array_2, array_1[i]) * array_1[i])

    return score


def count_instances(array, value):

    count = 0

    for i in range(len(array)):
        if array[i] == value:
            count += 1

    return count


list_c = []
list_d = []

# Real data
f = open("day_1_input.txt", "r")
for line in f:
    pair = re.findall(r"\d+", line)
    list_c.append(int(pair[0]))
    list_d.append(int(pair[1]))
f.close()

print(similarity_score(list_c, list_d))
