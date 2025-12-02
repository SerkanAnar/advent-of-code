def recurse(target, numbers, current_result):
    if not numbers:
        return current_result == target
    
    if recurse(target, numbers[1:], current_result + numbers[0]):
        return True
    
    if recurse(target, numbers[1:], current_result * numbers[0]):
        return True
            
with open('input.txt') as f:
    lines = f.readlines()

equations = {}
for line in lines:
    line = line.strip()
    target, operands = line.split(':')
    operands = list(map(int, operands.split()))
    equations[int(target)] = operands

total_sum = 0
for key in equations:
    operands = equations[key]
    if recurse(key, operands[1:], operands[0]):
        total_sum += key
print(total_sum)