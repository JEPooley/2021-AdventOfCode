# Day 9 : Smoke Basin

## Part 2


import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from collections import Counter

# open data
data = open("data.txt").read().split("\n")
array = np.array([list(row) for row in data], dtype=int)

# get basins
basins = label(array < 9, connectivity=1)

# find largest
counter = Counter(basins.flatten())
counter.pop(0)
top_3 = counter.most_common(3)

# calculate product
print(np.prod([count for _, count in top_3]))