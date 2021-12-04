# Day 4 : Giant Squid

## Part 2


import numpy as np
from itertools import product


class Card:
    
    def __init__(self, card_numbers):
        self.numbers = card_numbers
        self.marked = np.zeros(self.numbers.shape).astype(bool)

    @property
    def shape(self):
        return self.numbers.shape

    def mark(self, number):
        self.marked[self.numbers == number] = True

    def won(self):
        if self.shape[0] in np.sum(self.marked, axis=0):
            return True
        elif self.shape[1] in np.sum(self.marked, axis=1):
            return True
        return False

    def __str__(self):
        return str(self.numbers)


# load data
card_numbers = np.recfromtxt("data.txt", skip_header=True).reshape(100, 5, 5)
call_numbers = np.array(open("data.txt", "r").readline().split(",")).astype(int)

# create cards
cards = [Card(numbers) for numbers in card_numbers]

# call numbers
win_order = {}
for card in cards:
    for i, number in enumerate(call_numbers):
        card.mark(number)
        if card.won():
            win_order[i] = (card, number)
            break

# find last winning card
latest = sorted(win_order, reverse=True)[0]
last_card, last_number = win_order[latest]

# calculate score
print(np.sum(last_card.numbers[~last_card.marked]) * last_number)