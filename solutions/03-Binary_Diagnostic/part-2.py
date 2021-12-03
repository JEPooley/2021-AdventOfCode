# Day 3 : Binary Diagnostics

## Part 2


import numpy as np
from itertools import count


def binary_to_decimal(bool_array):
    decimal_Values = 1 << np.arange(bool_array.size)[::-1]
    return bool_array.dot(decimal_Values)


def filter_column(array_2d, position, value):
    filtered_columns = filter(lambda row: row[position] == value, array_2d)
    return np.array(list(filtered_columns))


def get_most_occuring(array_2d, position):
    column_mean = np.mean(array_2d[:, position])
    return column_mean >= 0.5


# load diagnostics
diagnostics = open("diagnostics.txt", "r").read().split("\n")

# seperate bits into array
diagnostics_array = np.array([list(bits) for bits in diagnostics]).astype(bool)

# get oxygen generator rating
column_count = count()
oxygen_generator = diagnostics_array.copy()
while len(oxygen_generator) > 1:
    column = next(column_count)
    most_occuring = get_most_occuring(oxygen_generator, column)
    oxygen_generator = filter_column(oxygen_generator, column, most_occuring)

# get CO2 scrubber rating
column_count = count()
co2_scrubber = diagnostics_array.copy()
while len(co2_scrubber) > 1:
    column = next(column_count)
    least_occuring = ~get_most_occuring(co2_scrubber, column)
    co2_scrubber = filter_column(co2_scrubber, column, least_occuring)

# calculate product
co2_scrubber_rating = binary_to_decimal(co2_scrubber[0])
oxygen_generator_rating = binary_to_decimal(oxygen_generator[0])
print(co2_scrubber_rating * oxygen_generator_rating)
