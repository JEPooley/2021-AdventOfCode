# Day 1 : Sonar Sweep

## Part 2

import numpy as np


# load measurements
measurements = np.recfromtxt("measurements.txt")

# get window totals
kernel = np.ones(3,dtype=int)
windowed_measurements = np.convolve(measurements, kernel, "valid")

# get increments
measurement_increments = np.diff(windowed_measurements)

# count positive increments
count_increases = np.sum(measurement_increments > 0)

print(count_increases)