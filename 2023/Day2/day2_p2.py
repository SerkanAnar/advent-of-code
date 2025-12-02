sum = 0; 

file = open("/Users/serkan/Documents/AoC 2023/Day2/input.txt", "r")
line = file.readline()
while line: 
    line = line.split()
    max_red = 0
    max_green = 0
    max_blue = 0
    for i in range(2, len(line), 2): 
        digit = int(line[i])
        color = line[i+1].replace(';', '').replace(',', '')
        if color == "red":
            if digit > max_red:
                max_red = digit
        elif color == "blue": 
            if digit > max_blue:
                max_blue = digit
        elif color == "green": 
            if digit > max_green: 
                max_green = digit
    sum += (max_red * max_blue * max_green)
    line = file.readline()
print(sum)