import sys

def p1(lines):
    val = 50
    result = 0
    for line in lines:
        turns = int(line[1:])
        if line.startswith('L'):
            val -= turns
        else:
            val += turns
        val %= 100
        if val == 0: result += 1
    return result

def p2(lines):
    old = 50
    result = 0
    for line in lines:
        turns = int(line[1:])
        if line.startswith('L'):
            new = old - turns
        else:
            new = old + turns
        if new == 0 or new == 100:
            result += 1
        elif new < 0:
            result += 1 + ((turns-old) // 100)
            if old == 0:
                result -= 1
        elif new > 100:
            result += 1 + ((turns-(100-old)) // 100)
        new %= 100
        old = new
    return result

if __name__ == '__main__':
    with sys.stdin as f:
        lines = [line.strip() for line in f.readlines()]
    print(f'part 1: {p1(lines)}')
    print(f'part 2: {p2(lines)}')