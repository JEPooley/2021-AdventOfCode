# Day 11 : Dumbo Octopus

## Part 2


import numpy as np
from scipy.ndimage.morphology import binary_dilation
from scipy.ndimage import generate_binary_structure
from functools import partial


# define dilation
selem = generate_binary_structure(2, 2)
dilate = partial(binary_dilation, structure=selem)


# define class to combine flashes
class FlashMask:

    def __init__(self, shape):
        self.shape = shape
        self.array = np.zeros(shape)
        self.count = 0
    
    def __add__(self, array):
        return array + self.array

    def __new_mask(self, i, j):
        mask = np.zeros(self.shape)
        mask[i, j] = 1
        return dilate(mask)

    def add(self, i, j):
        mask = self.__new_mask(i, j)
        self.array += mask
        self.count += 1

    def reset(self):
        self.array = np.zeros(self.shape)


# load octopi
octopi = open("octopi.txt").read().split("\n")
octopi = np.array([list(o) for o in octopi], dtype=int)


# initialise flash mask
flash_mask = FlashMask(octopi.shape)


# iterate days
n_days = 100
all_flashing = False
day = 0
while not all_flashing:

    # Add 1 to all
    octopi += 1

    # find flashes
    flashes = octopi > 9
    
    # while there are more to flash, keep flashing!
    while np.sum(flashes) > 0:

        # Add flashes
        for i, j in np.argwhere(flashes):
            flash_mask.add(i, j)
        octopi = flash_mask + octopi

        # update params
        octopi[flashes] = -np.inf
        flashes = octopi > 9
        flash_mask.reset()
        
    # check if all octopi flashing
    if np.sum(octopi == -np.inf) == octopi.size:
        all_flashing = True

    # Set flashers to 0 energy
    octopi[octopi == -np.inf] = 0
    
    day += 1

# print day when all flashing
print(day)