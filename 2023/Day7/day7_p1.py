file = open("input.txt", "r")
sorted = []
hands = []
line = file.readline()
while line: 
    hands.append(tuple(line.strip().split()))
    line = file.readline()
print(hands)

# Approach
# Sort from strongest to weakest GLOBALLY
# Then sort them within categories
for i in range(0, len(hands)):
    dictionary = {
        "five": 1,
        "four": 1, 
        "full": 1, 
        "three": 1, 
        "two": 1, 
        "one": 1, 
        "high": 1
    }
    hand_bid = hands[i]
    hand = hand_bid[0]
    
    break