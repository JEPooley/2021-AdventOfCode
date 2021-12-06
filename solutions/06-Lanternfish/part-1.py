# Day 6 : Lanternfish

## Part 1


import numpy as np


# import ages
ages = np.genfromtxt("ages.txt", dtype=None, delimiter=',', encoding=None)

# iterate days
n_days = 80
for day in range(n_days):
    giving_birth = ages == 0
    ages[giving_birth] = 7
    ages = np.append(ages, [9] * np.count_nonzero(giving_birth))
    ages -= 1

# get population count
print(len(ages))