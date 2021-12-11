# Day 10 : Syntax Scoring

## Part 1


from collections import Counter


# define scores
scores = {">": 25137, "]": 57, ")": 3, "}": 1197}

# define bracket mappings
openers = {"<": ">", "[": "]", "(": ")", "{": "}"}
closers = {">": "<", "]": "[", ")": "(", "}": "{"}


def find_syntax_error(line):
    open_chunks = []
    for char in line:
        if char in openers:
            open_chunks.append(char)
        elif open_chunks[-1] == closers[char]:
            open_chunks.pop()
        else:
            return char


# open navigation_subsystem
navigation_subsystem = open("navigation.txt").read().split("\n")

# find syntax error score
score = 0
for line in navigation_subsystem:
    error = find_syntax_error(line)
    if error is not None:
        score += scores[error]
print(score)