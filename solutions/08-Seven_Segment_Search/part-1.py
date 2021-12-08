# Day 8 : Seven Segment Search

## Part 1


import numpy as np


# open digits
digits = open("digits.txt").read().split("\n")
patterns, output = zip(*(d.split(" | ") for d in digits))

# turn outputs into flattened array
output_array = np.array([o.split() for o in output]).flatten()

# get string lengths
lengths = np.vectorize(lambda s: len(s))(output_array)

# count occurences of 1, 4, 7, 8
print(np.sum(np.isin(lengths, [2, 3, 4, 7])))