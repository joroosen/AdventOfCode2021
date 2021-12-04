with open('day3_input.txt') as f:
    lines = f.read().splitlines()

array_input = []

for line in lines:
    temp_array = []
    for a in line:
        temp_array.append(a)
    array_input.append(temp_array)

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

rotated_array = rotated(array_input)
gamma = []
epsilon = []

for a in rotated_array:
    if a.count('1') > a.count('0'):
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

strings = [str(integer) for integer in gamma]
a_string = "".join(strings)
gamma = a_string
strings = [str(integer) for integer in epsilon]
b_string = "".join(strings)
epsilon = b_string

print("Day 3: " + str((int(gamma, 2) * int(epsilon, 2))))


