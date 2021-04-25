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

    print("-"*10)
    return


input1 = []
input2 = []
input3 = []

random_inputs = []

for i in range(10):
    temp = []
    for j in range(random.randint(4, 14)):
        start = random.randint(0, 20)
        finish = random.randint(start+1, 24)
        weight = random.randint(0, 20)
        temp.append((start, finish, weight))
    random_inputs.append(temp)
