# Day 1 : Sonar Sweep

## Part 1

import numpy as np


# load measurements
measurements = np.recfromtxt("measurements.txt")

# get increments
measurement_increments = np.diff(measurements)

# count positive increments
count_increases = np.sum(measurement_increments > 0)

print(count_increases)