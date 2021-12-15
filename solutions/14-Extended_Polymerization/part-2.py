# Day 14 : Extended Polymerization

## Part 2


from collections import defaultdict


# load rules
text = open("rules.txt").read().split("\n\n")
seed = text[0]
rules = [rule.split(" -> ") for rule in text[1].split("\n")]


# create insertion map
pair_map = {key: (key[0] + value, value + key[1]) for key, value in rules}
insertion_map = {key: value for key, value in rules}


# initialise pair counter
pair_count = defaultdict(int)
for i in range(len(seed) - 1):
    pair = seed[i:i+2]
    pair_count[pair] += 1


# initialise char counter
char_count = defaultdict(int)
for char in seed:
    char_count[char] += 1


# iterate polymerisation
steps = 40
for _ in range(steps):
    new_pair_count = defaultdict(int)
    for pair, count in pair_count.items():
        p1, p2 = pair_map[pair]
        new_pair_count[p1] += count
        new_pair_count[p2] += count
        new_char = insertion_map[pair]
        char_count[new_char] += count
    pair_count = new_pair_count.copy()


# get most and least occuring
most_occuring = max(char_count, key=char_count.get)
least_occuring = min(char_count, key=char_count.get)


print(char_count[most_occuring] - char_count[least_occuring])