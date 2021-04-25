"""
Given n number of requests
    s(i) start time
    f(i) finish time
    s(i) < f(i)
Two requests are compatible if they don't overlap
    i.e. f(i) <= s(j) or f(j) <= s(i)

Goal: Select a compatible subset of requests of maximum size
"""


def greedy_interval_scheduling(input_list):
    """
    @params
        input_list: list of sets of start and finish time
        e.g. [(1, 3), (2, 4), (5, 10)]
    @returns
        list with maximum number of requests
    """

    result = []

    # Sort the requests by their finish time
    requests = sorted(input_list, key=lambda item: item[1])

    while requests:
        # Select the item with the earliest finish time
        current = requests.pop(0)

        overlap = True
        while overlap and requests:
            overlap = False
            # Remove the request if start time overlaps with the previous finish time
            if requests[0][0] <= current[1]:
                requests.pop(0)
                overlap = True

        result.append(current)

    return result
