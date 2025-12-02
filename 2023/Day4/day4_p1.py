file = open("input.txt", "r")
line = file.readline()
sum = 0

while line: 
    winning_numbers = 0
    points = 0
    winning_nums, nums_on_card = [part.strip().split() for part in line.split('|')]
    nums_on_card = [num for num in nums_on_card if num]
    winning_nums = [num for num in winning_nums[2:] if num]
    
    for number in nums_on_card:
        if number in winning_nums:
            winning_numbers += 1
    if winning_numbers > 0:
        points += 1
    for i in range(0, winning_numbers-1): 
        points *= 2
    sum += points
    line = file.readline()
print(sum)