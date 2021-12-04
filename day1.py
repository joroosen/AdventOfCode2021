# Part 1
with open('day1_input.txt') as f:
    lines = f.readlines()
depth = 999999
increased = 0

list_of_lists = []
for line in lines:
  stripped_line = line.strip()
  list_of_lists.append(int(stripped_line))

for a in list_of_lists:
    if a > depth:
        increased += 1
    depth = a

print("Day 1 Part 1: " + str(increased))

# Part 2

depth = 999999
increased = 0
windows = []

for i in range(len(list_of_lists)):
    if i < (len(list_of_lists) - 2):
        windows.append(list_of_lists[i] + list_of_lists[i + 1] + list_of_lists[i + 2])

print(windows)

for a in windows:
    if a > depth:
        increased += 1
    depth = a

print("Day 1 Part 2: " + str(increased))

