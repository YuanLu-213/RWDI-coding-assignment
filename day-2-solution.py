##Reading data from data file and save them as tuples in a list
with open('input_day2.txt') as file:
    lines = file.readlines()
    data = []
    for line in lines:
        cmd = line.strip().split()
        data.append((cmd[0], int(cmd[1])))

##Part-1:
##Function to find the horizontal times depth
def findDestinationMultiple(data):
    horizontal = 0
    depth = 0

    for cmd in data:
        if cmd[0] == "forward":
            horizontal += cmd[1]
        elif cmd[0] == "down":
            depth += cmd[1]
        else:
            depth -= cmd[1]
    
    return horizontal * depth

print(f'Answer is: {findDestinationMultiple(data)}')

##Part-2:
##Function to find the horizontal times depth with aim
def findMultipleWithAim(data):
    horizontal, depth, aim = 0, 0, 0

    for cmd in data:
        if cmd[0] == "forward":
            horizontal += cmd[1]
            depth += (aim * cmd[1])
        elif cmd[0] == "down":
            aim += cmd[1]
        else:
            aim -= cmd[1]
    
    return horizontal * depth

print(f'Answer is: {findMultipleWithAim(data)}')