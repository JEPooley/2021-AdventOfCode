# Day 3 : Binary Diagnostics

## Part 1


import numpy as np


def binary_to_decimal(bool_array):
    decimal_Values = 1 << np.arange(bool_array.size)[::-1]
    return bool_array.dot(decimal_Values)


# load diagnostics
diagnostics = open("diagnostics.txt", "r").read().split("\n")

# seperate bits into array
diagnostics_array = np.array([list(bits) for bits in diagnostics]).astype(bool)

# get readings
gamma_rate = np.median(diagnostics_array, axis=0).astype(bool)
epsilon_rate = ~gamma_rate

# calculate product
print(binary_to_decimal(epsilon_rate) * binary_to_decimal(gamma_rate))
