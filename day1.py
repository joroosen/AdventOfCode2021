with open('day1_input.txt') as f:
    lines = f.readlines()
depth = 999999
increased = 0
for line in lines:
    if int(line.strip()) > depth:
        increased += 1
    depth = int(line.strip())

print(increased)