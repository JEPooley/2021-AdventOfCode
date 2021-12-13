# Day 13 : Transparent Origami

## Part 1


import numpy as np
import matplotlib.pyplot as plt


class Paper:
    
    def __init__(self, dots_x, dots_y):
        self.x = dots_x
        self.y = dots_y
    
    def fold(self, direction, position):
        if direction.lower() == "y":
            self.y[self.y > position] = 2 * position - self.y[self.y > position]
        elif direction.lower() == "x":
            self.x[self.x > position] = 2 * position - self.x[self.x > position]
    
    def count(self):
        coords = list(zip(self.x, self.y))
        return len(set(coords))

    @classmethod
    def from_tuples(cls, dot_coords):
        x, y = list(zip(*dot_coords))
        return Paper(np.array(x), np.array(y))
    
    def plot(self):
        scatter = plt.scatter(self.x, self.y)
        ax = scatter.axes
        ax.invert_yaxis()
        plt.show()


# load instructions
all_instructions = open("instructions.txt").read().split("\n\n")
folds = all_instructions[1].split("\n")
dots = np.array([s.split(",") for s in all_instructions[0].split("\n")], dtype=int)


# create Paper object
paper = Paper.from_tuples(dots)


# fold
for fold in folds:
    direction, position = fold.split("=")
    paper.fold(direction[-1], int(position))


# plot dots
paper.plot()