# Day 7 : The Treachery of Whales

## Part 2


import numpy as np


def sum_range(n):
    return 0.5 * n * (n + 1)

def distance(array, number):
    difference = np.abs(np.subtract(array, number))
    costs = np.vectorize(sum_range)(difference)
    return np.sum(costs)


# import positions
positions = np.genfromtxt("positions.txt",
                          dtype=None,
                          delimiter=',',
                          encoding=None)


# brute force
cost = {}
for i in range(np.max(positions)):
    cost[i] = distance(positions, i)


# get least distance
print(min(cost.values()))