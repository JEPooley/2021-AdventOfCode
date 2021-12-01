# Day 1 : Sonar Sweep

## Part 1

import numpy as np


# load measurements
measurements = np.recfromtxt("measurements.txt")

# get increments
measurement_increments = np.diff(measurements)

# count positive increments
increases = np.where(measurement_increments > 0, 1, 0)
count_increases = np.sum(increases)

print(count_increases)