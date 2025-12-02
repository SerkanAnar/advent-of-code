def getSymbols():
    symbols = []
    val = 33
    for i in range(val, 48):
        symbols.append(chr(i))
    return symbols

sum = 0
file = open('/Users/serkan/Documents/AoC 2023/Day3/input.txt', 'r')
prev = ''
curr = file.readline()
symbols = getSymbols()
added = False
while curr: 
    next = file.readline()
    currNum = ''
    number = []
    indices = []
    temporary = []
    temporary2 = []
    for i in range(0, len(curr)):
        if curr[i].isdigit():
            currNum += curr[i]
            temporary2.append(curr[i])
            temporary.append(i)
        elif currNum: 
            number.append(temporary2)
            indices.append(temporary)
            temporary2 = []
            temporary = []
            currNum = ''
    # Now, check the conditions and do things appropriately
    for i in range(0, len(indices)):
        num_string = ''
        num = int(num_string.join(number[i]))
        size = len(indices[i])
        digit1_index = indices[i][0]
        digit2_index = indices[i][-1]
        for index in indices[i]: 
            if next and next[index] in symbols:
                sum += num
                continue
            elif prev and next[index] in symbols:
                sum += num
                continue
        if curr[digit1_index-1] in symbols or curr[digit2_index+1] in symbols:
            sum += num
            continue
        elif prev and prev[digit1_index-1] or prev[digit2_index+1] in symbols:
            sum += num
            continue
        elif next and next[digit1_index-1] or next[digit2_index+1] in symbols: 
            sum += num
            continue
    prev = curr
    curr = file.readline()
print(number)
print(indices)
print(sum)
    