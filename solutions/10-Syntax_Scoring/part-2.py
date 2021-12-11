# Day 10 : Syntax Scoring

## Part 2


from collections import Counter


# define scores
scores = {">": 4, "]": 2, ")": 1, "}": 3}

# define bracket mappings
openers = {"<": ">", "[": "]", "(": ")", "{": "}"}
closers = {">": "<", "]": "[", ")": "(", "}": "{"}


def calculate_score(close_chunks):
    score = 0
    for char in close_chunks:
        score *= 5
        score += scores[char]
    return score

def score_line(line):
    open_chunks = []
    for char in line:
        if char in openers:
            open_chunks.append(char)
        elif open_chunks[-1] == closers[char]:
            open_chunks.pop()
        else:
            return -1
    
    close_chunks = reversed([openers[char] for char in open_chunks])
    return calculate_score(close_chunks)

# open navigation_subsystem
navigation_subsystem = open("navigation.txt").read().split("\n")

# score lines
line_scores = []
for line in navigation_subsystem:
    score = score_line(line)
    if score >= 0:
        line_scores.append(score)
    
# get middle
idx = int((len(line_scores) - 1) / 2)
print(sorted(line_scores)[idx])

