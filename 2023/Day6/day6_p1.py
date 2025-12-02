file = open("input.txt", "r")
time = file.readline().split()[1:]
distance = file.readline().split()[1:]
ways_to_win = []

for i in range(0, len(distance)): 
    counter = 0
    dist = int(distance[i])
    total_ms = int(time[i])
    for j in range(0, total_ms):
        time_holding = j
        time_moving = (total_ms - time_holding) * time_holding
        if time_moving > dist:
            counter += 1
    ways_to_win.append(counter)

product = 1
for i in range(0, len(ways_to_win)):
    product *= ways_to_win[i]

print(product)