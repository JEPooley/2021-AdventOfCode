# Day 14 : Extended Polymerization

## Part 1


import re
from collections import Counter


def argstring(string, substring):
    return [m.start() + 1 for m in re.finditer(f"(?={substring})", string)]


def insert_elements(insertion_map, string):
    insertions = {}
    for key, value in insertion_map.items():
        idxs = argstring(string, key)
        insertions.update({idx: value for idx in idxs})
    for idx in sorted(insertions, reverse=True):
        value = insertions[idx]
        string = string[:idx] + value + string[idx:]
    return string


# load rules
text = open("rules.txt").read().split("\n\n")
seed = text[0]
rules = [rule.split(" -> ") for rule in text[1].split("\n")]


# create insertion map
insertion_map = {key: value for key, value in rules}


# insert elements
steps = 10
for i in range(steps):
    seed = insert_elements(insertion_map, seed)


# find most and least common
counter = Counter(seed)
most_common = counter.most_common()[0]
least_common = counter.most_common()[-1]
print(most_common[1] - least_common[1])