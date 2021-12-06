# Day 6 : Lanternfish

## Part 2


import numpy as np


# import ages
ages = np.genfromtxt("ages.txt", dtype=None, delimiter=',', encoding=None)

# create array - counts of each age group positionally
counts = np.zeros(9)

# populate positional counts
for age in ages:
    counts[age] += 1

# iterate days
n_days = 256
for day in range(n_days):
    giving_birth = counts[0]
    counts = np.roll(counts, -1)
    counts[6] += giving_birth

# get population count
print(np.sum(counts))