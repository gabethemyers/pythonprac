with open(r'C:\Users\Gabe\pythonprac\AdventofCode2021\day2\input.txt', 'r') as file:
       input_list = file.readlines() 
       input_list = [line.rstrip() for line in input_list]
        
meowlist = ['foward 5', 'down 5', 'foward 8', 'up 3', 'down 8', 'foward 2']

def part1positions(alist):
    hpos = 0
    depth = 0
    new_list = []
    for elem in alist:
        new_list.append(tuple(elem.split(' ')))
    for elem in new_list:
        if elem[0] == 'forward':
            hpos += int(elem[1])
        elif elem[0] == 'up':
            depth -= int(elem[1])
        elif elem[0] == 'down':
            depth += int(elem[1])
        print(hpos, depth)
    return hpos * depth


def part2pos(alist):
    hpos = 0
    depth = 0
    aim = 0
    new_list = []
    for elem in alist:
        new_list.append(tuple(elem.split(' ')))
    for elem in new_list:
        if elem[0] == 'forward':
            hpos += int(elem[1])
            if aim != 0:
                depth += aim * int(elem[1])
        elif elem[0] == 'up':
            aim -= int(elem[1])
        elif elem[0] == 'down':
            aim += int(elem[1])
        print(hpos, depth, aim)
    return hpos * depth
        
print(part2pos(input_list))