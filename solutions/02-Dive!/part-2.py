# Day 2 : Dive!

## Part 2


import numpy as np
from collections import defaultdict


class Submarine:
    
    def __init__(self):
        self.forward = 0
        self.depth = 0
        self.aim = 0
    
    def move(self, instruction: str, distance: int):
        if instruction == "forward":
            self.forward += distance
            self.depth += distance * self.aim
        elif instruction == "up":
            self.aim -= distance
        elif instruction == "down":
            self.aim += distance


# load moves
moves = open("moves.txt", "r").read().split("\n")

# run all moves
submarine = Submarine()
for move in moves:
    intsruction, distance = move.split()
    submarine.move(intsruction, int(distance))

# multiply distances
print(submarine.depth * submarine.forward)