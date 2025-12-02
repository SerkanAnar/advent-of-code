# Can only go in one direction ... 
dictionary = {
    '|': "up",
    '-': "right", 
    'L': "left-up",
    'J': "down-left",
    '7': "right-down", 
    'F': "up-right", 
    '.': "nothing", 
    'S': "start"
}
found = False
file = open("input.txt", "r")
adjacency = []
for line in file: 
    adjacency.append([x for x in line.strip().split()])

for i in range(0, len(adjacency)):
    for j in range(0, len(adjacency[i])):
        if adjacency[i][0][j] == 'S':
            position = (i, j)
            
# Starting position acquired
# Directions down, left, right, down
queue = []
queue.append(position)
position = queue.pop(0)
while not found: 
    adjacents = []
    
    # The below 4 rows are characters, not positions
    
    print("position is: ", position)
    if position[0] - 1 >= 0: 
        adjacent_up = adjacency[position[0] - 1][0][position[1]]
        adjacents.append(adjacent_up)
    
    if position[0] + 1 < len(adjacency):
        adjacent_down = adjacency[position[0] + 1][0][position[1]]
        adjacents.append(adjacent_down)
        
    if position[1] - 1 >= 0: 
        adjacent_left = adjacency[position[0]][0][position[1] - 1]
        adjacents.append(adjacent_left)
        
    if position[1] + 1 < len(adjacency[position[0]][0]):
        adjacent_right = adjacency[position[0]][0][position[1] + 1]
        adjacents.append(adjacent_right)
        
    
    for i in range(0, len(adjacents)):
        
        if dictionary[adjacents[i]] == "nothing":
            continue
        if dictionary[adjacents[i]] == "up": 
            queue.append((position[0] - 1, position[1]))
        if dictionary[adjacents[i]] == "right": 
            queue.append((position[0], position[1]+1))
        if dictionary[adjacents[i]] == "left-up":
            queue.append((position[0] - 1, position[1] - 1))
        if dictionary[adjacents[i]] == "down-left":
            queue.append((position[0] + 1, position[1] - 1))
        if dictionary[adjacents[i]] == "right-down":
            queue.append((position[0] + 1, position[1] + 1))
        if dictionary[adjacents[i]] == "up-right":
            queue.append((position[0] - 1, position[1] + 1))
            
    print("queue is ", queue)
    print("adjacents is ", adjacents)
    position = queue.pop(0)
    print("position is ", position)
    if adjacency[position[0]][0][position[1]] == 'S':
        found = True
print(found)