horizontal = 0
depth = 0


with open('day2_input.txt') as f:
    lines = f.read().splitlines()

for a in lines:
    if a.split(' ')[0] == "forward":
        horizontal = horizontal + int(a.split(' ')[1])
    elif a.split(' ')[0] == "down":
        depth = depth + int(a.split(' ')[1])
    elif a.split(' ')[0] == "up":
        depth = depth - int(a.split(' ')[1])

print("Day 2 Part 1 : " + str(horizontal*depth))


horizontal = 0
depth = 0
aim = 0

for a in lines:
    if a.split(' ')[0] == "forward":
        horizontal = horizontal + int(a.split(' ')[1])
        depth = depth + (aim * int(a.split(' ')[1]))
    elif a.split(' ')[0] == "down":
        aim = aim + int(a.split(' ')[1])
    elif a.split(' ')[0] == "up":
        aim = aim - int(a.split(' ')[1])

print(horizontal * depth)






