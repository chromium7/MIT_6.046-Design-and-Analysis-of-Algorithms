"""
Test the greedy algorithm function
"""

import random
from greedy_is import greedy_interval_scheduling


def test(inp):
    print("Input:")
    print(inp)

    result = greedy_interval_scheduling(inp)

    print("Result:")
    print("Count:", len(result))
    print("Time:", result)

    print("-"*10)
    return


# Input list of start and finish time
input1 = [
    (5, 14),
    (6, 9),
    (10, 12)
]
input2 = [
    (7, 14),
    (5, 9),
    (10, 13),
    (6, 7),
    (8, 11),
    (12, 15)
]
input3 = [
    (5, 8),
    (9, 12),
    (13, 16),
    (17, 20),
    (7, 10),
    (7, 10),
    (7, 10),
    (11, 14),
    (15, 18),
    (15, 18),
    (15, 18)
]

# Randomized inputs
random_inputs = []

for i in range(10):
    temp = []
    for j in range(random.randint(4, 14)):
        start = random.randint(0, 20)
        finish = random.randint(start+1, 24)
        temp.append((start, finish))
    random_inputs.append(temp)

print("Static tests:")
print("-"*10)
test(input1)
test(input2)
test(input3)

print("Random tests:")
print("-"*10)
for inp in random_inputs:
    test(inp)
