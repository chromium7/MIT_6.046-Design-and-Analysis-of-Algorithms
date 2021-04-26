"""
Variation of the basic interval scheduling
Each request is given a certain weight
Get the set of requests with maximum weight

Solution time complexity is O(N^2)
"""


def find_latest_non_conflicting_request(requests, n):
    # Iterate from index n backwards
    for i in range(n-1, -1, -1):
        # Check if start time does not overlap with the finish time
        if requests[i][1] < requests[n][0]:
            return i

    # No non conflicting request available
    return -1


def get_weight(requests):
    # Get sum of weight of requests
    return sum([request[2] for request in requests])


def dp_interval_scheduling(input_list):
    """
    @params
        input_list: list of sets of start time, finish time and weight
        e.g. [(1, 3, 40), (2, 4, 50), (5, 10, 30)]
    @returns
        list with maximum number of requests
    """
    # Sort the requests by their finish time
    requests = sorted(input_list, key=lambda item: item[1])

    memo = [[]] * len(requests)

    for i in range(len(requests)):
        # Get non conflicting index
        index = find_latest_non_conflicting_request(requests, i)

        move = [requests[i]]

        # If there is valid non conflicting request
        # add that request set to the current set
        if index != -1:
            move += memo[index]

        if i > 0:
            # Get set of request with max weight
            # compare the current set with the previous best set
            prev_move = memo[i-1]
            if get_weight(prev_move) > get_weight(move):
                move = prev_move

        # Store to the memo
        memo[i] = move

    # Return set of requests with max weight
    return memo[-1]
