# Day 9 : Smoke Basin

## Part 1


import numpy as np
from scipy.ndimage import minimum_filter


# open data
data = open("data.txt").read().split("\n")
array = np.array([list(row) for row in data], dtype=int)

# get minimum of each cell
selem = np.array([[False, True, False], [True, False, True], [False, True, False]])
min_array = minimum_filter(array, footprint=selem, mode="constant", cval=10)

# find minima
minima = array[min_array > array]

# calculate risk
print(np.sum(minima + 1))