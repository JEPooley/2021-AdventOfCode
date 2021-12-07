# Day 7 : The Treachery of Whales

## Part 1


import numpy as np


# import positions
positions = np.genfromtxt("positions.txt",
                          dtype=None,
                          delimiter=',',
                          encoding=None)


# find the median
median = np.median(positions)


# find the cost
print(np.sum(np.abs(np.subtract(positions, median))))