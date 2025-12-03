import sys

def p1(lines):
    res = 0
    for line in lines:
        largest = -1
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                joltage = int(line[i]+line[j])
                if joltage > largest: largest = joltage
        res += largest
    print(res)

def p2(lines):
    pass

if __name__ == '__main__':
    with sys.stdin as f:
        lines = [line.strip() for line in f.readlines()]
    
    p1(lines)
    # p2(lines)
