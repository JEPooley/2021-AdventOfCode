# Day 5 : Hydrothermal Venture

## Part 1


import numpy as np
from collections import Counter


class Line:

    def __init__(self, start_coord, end_coord):
        self.start_coord = start_coord
        self.end_coord = end_coord
        self.change = np.subtract(end_coord, start_coord)

    @property
    def is_orthoganol(self):
        return np.any(self.change == 0)

    @classmethod
    def from_string(cls, string):
        string_coords = string.split(" -> ")
        start_coord = np.array([int(c) for c in string_coords[0].split(",")])
        end_coord = np.array([int(c) for c in string_coords[1].split(",")])
        return Line(start_coord, end_coord)

    @staticmethod
    def get_range(start, stop):
        if start == stop:
            return np.array([start])

        _min, _max = sorted([start, stop])
        return np.arange(_min, _max + 1)

    def coords(self):
        x_range = self.get_range(self.start_coord[0], self.end_coord[0])
        y_range = self.get_range(self.start_coord[1], self.end_coord[1])
        x, y = np.meshgrid(x_range, y_range)
        return np.vstack(list(zip(x.ravel(), y.ravel())))


# load lines
line_strings = open("lines.txt").read().split("\n")

# convert to Line objects
lines = [Line.from_string(string) for string in line_strings]

# evaluate line coords
all_coords = []
for line in lines:
    if line.is_orthoganol:
        all_coords.extend(line.coords())

# convert to hashable type
tuple_coords = [tuple(coord) for coord in all_coords]

# find repeated coordinates
counts = Counter(tuple_coords)
print(sum(1 for value in counts.values() if value > 1))