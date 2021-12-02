# Day 2 : Dive!

## Part 1


# load moves
moves = open("moves.txt", "r").read().split("\n")

# total each instruction type
moves_count = {"down": 0, "up": 0, "forward": 0}
for move in moves:
    instruction, distance = move.split()
    moves_count[instruction] += int(distance)

horizontal_pos = moves_count["forward"]
vertical_pos = moves_count["down"] - moves_count["up"]

# multiply distances
print(horizontal_pos * vertical_pos)