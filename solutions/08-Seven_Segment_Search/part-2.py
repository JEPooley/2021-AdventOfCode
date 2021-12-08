# Day 8 : Seven Segment Search

## Part 2


'''
Rules:

1. 1, 4, 7, 8 have two, four, three, seven active sections respectively
2. 6 has six active sections AND shares only one of them with 1
3. 9 has six active sections AND shares four of them with 4
4. 0 has six active sections AND shares three of them with 4
5. 3 has five active sections AND shares two of them with 1
6. 2 has five active sections AND all of its sections are in 6's
7. 5 has five active sections AND all of its sections are in 9's
'''

from collections import defaultdict


def get_lengths(pattern):
    lengths = defaultdict(list)
    for digit in pattern:
        lengths[len(digit)].append(digit)
    return lengths


def get_map(pattern):
    lengths = get_lengths(pattern)

    # Rule 1 
    digit_map = {1: lengths[2][0], 4: lengths[4][0], 7: lengths[3][0], 8: lengths[7][0]}
    
    # Rules 2, 3 & 4
    for digit in lengths[6]:
        intersected = digit.intersection(digit_map[1])
        if len(intersected) == 1:
            digit_map[6] = digit
        else:
            intersected = digit.intersection(digit_map[4])
            if len(intersected) == 4:
                digit_map[9] = digit
            else:
                digit_map[0] = digit

    # Rules 5, 6 & 7
    for digit in lengths[5]:
        intersected = digit.intersection(digit_map[1])
        if len(intersected) == 2:
            digit_map[3] = digit
        else:
            intersected = digit.intersection(digit_map[9])
            if len(intersected) == 4:
                digit_map[2] = digit
            else:
                digit_map[5] = digit
    
    return digit_map


class Decoder:
    
    def __init__(self, digit_string):
        self.__digits = self.__format_digits(digit_string)
        self.__digit_map = get_map(self.__digits)
    
    @property
    def digit_map(self):
        return self.__digit_map

    @staticmethod
    def __format_digits(pattern_string):
        pattern_list = pattern_string.split()
        return [set(digit) for digit in pattern_list]

    def __call__(self, digit_string):
        output = ""
        for input_digit in [set(d) for d in digit_string.split()]:
            for value, digit in self.digit_map.items():
                if input_digit == digit:
                    output += str(value)
                    break
        return int(output)


# open digits
digits = open("digits.txt").read().split("\n")
patterns, outputs = zip(*(d.split(" | ") for d in digits))

# create decoders
decoders = [Decoder(pattern) for pattern in patterns]

# calculate values
values = [decoder(output) for decoder, output in zip(decoders, outputs)]

# calculate sum
print(sum(values))