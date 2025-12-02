sum = 0; 
max_red = 12
max_green = 13
max_blue = 14

file = open("/Users/serkan/Documents/AoC 2023/Day2/input.txt", "r")
line = file.readline()
while line: 
    line = line.split()
    broken = False
    for i in range(2, len(line), 2): 
        digit = int(line[i])
        color = line[i+1].replace(';', '').replace(',', '')
        if color == "red":
            if digit > max_red:
                broken = True
                break
        elif color == "blue": 
            if digit > max_blue:
                broken = True
                break
        elif color == "green": 
            if digit > max_green: 
                broken = True
                break
    if not broken: 
        sum += int(line[1].replace(':', ''))
    line = file.readline()
print(sum)