import sys

def p1(nums):
    res = []
    for num in nums:
        if len(num) % 2 == 1: continue
        mid_point = len(num) // 2
        if num[:mid_point] == (num[mid_point:]):
            res.append(int(num))
    return sum(res)

def p2(nums):
    res = []
    for num in nums:
        for i in range(len(num) // 2):
            substr = num[:i+1]
            rest = num[i+1:]
            for j in range(0, len(rest), i+1):
                if substr != rest[j:j+i+1]:
                    break
            else:
                res.append(int(num))
                break
    return sum(res)

if __name__ == '__main__':
    with sys.stdin as f:
        line = f.readline().strip()
    ranges = line.split(',')
    nums = []
    for num_range in ranges:
        start, end = map(int, num_range.split('-'))
        nums.extend(map(str, list(range(start, end+1))))
    
    print(f'part 1: {p1(nums)}')
    print(f'part 2: {p2(nums)}')