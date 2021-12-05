# Day 5 : Hydrothermal Venture

## Part 2


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
        elif stop > start:
            return np.arange(start, stop + 1)
        else:
            return np.arange(stop, start + 1)[::-1]
    
    @staticmethod
    def zip_coords(x, y):
        return list(zip(x.ravel(), y.ravel()))

    def coords(self):
        x_range = self.get_range(self.start_coord[0], self.end_coord[0])
        y_range = self.get_range(self.start_coord[1], self.end_coord[1])

        if self.is_orthoganol:
            x, y = np.meshgrid(x_range, y_range)
            return np.vstack(self.zip_coords(x, y))
        else:
            return np.array(self.zip_coords(x_range, y_range))


# load lines
line_strings = open("lines.txt").read().split("\n")

# convert to Line objects
lines = [Line.from_string(string) for string in line_strings]

# evaluate line coords
all_coords = []
for line in lines:
    all_coords.extend(line.coords())

# convert to hashable type
tuple_coords = [tuple(coord) for coord in all_coords]

# find repeated coordinates
counts = Counter(tuple_coords)
print(sum(1 for value in counts.values() if value > 1))