file = open("input.txt", "r")
time = int("".join(file.readline().split()[1:]))
distance = int("".join(file.readline().split()[1:]))
counter  = 0

for i in range(0, time):
    time_holding = i
    time_moving = (time - time_holding) * time_holding
    if time_moving > distance:
        counter += 1
print(counter)