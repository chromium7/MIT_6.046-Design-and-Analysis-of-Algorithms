"""
Test the dynamic programming algorithm function
"""

import random
from dp_weighted_is import dp_interval_scheduling


def test(inp):
    print("Input:")
    print(inp)

    result = dp_interval_scheduling(inp)

    print("Result:")
    print("Count:", len(result))
    print("Time:", result)
    print("Max weight:", sum([request[2] for request in result]))

    print("-"*10)
    return


input1 = [
    (0, 6, 60),
    (1, 4, 30),
    (3, 5, 10),
    (5, 7, 30),
    (5, 9, 50),
    (7, 8, 10)
]
input2 = [
    (5, 14, 70),
    (6, 9, 20),
    (10, 12, 40)
]
input3 = [
    (7, 14, 40),
    (5, 9, 100),
    (10, 13, 80),
    (6, 7, 40),
    (8, 11, 50),
    (12, 15, 70)
]

random_inputs = []

for i in range(10):
    temp = []
    for j in range(random.randint(4, 14)):
        start = random.randint(0, 20)
        finish = random.randint(start+1, 24)
        weight = random.randint(20, 100)
        temp.append((start, finish, weight))
    random_inputs.append(temp)

print("Fixed tests:")
print("-"*10)
test(input1)
test(input2)
test(input3)

print("Random tests:")
print("-"*10)
for inp in random_inputs:
    test(inp)
