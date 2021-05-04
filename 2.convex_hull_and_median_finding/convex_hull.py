"""
Given a set of point coordinates (x, y)
    assume no two have same x coordinate
    no two have same y coordinate
    no three in a line
Find convex hull (CH(S)): smallest polygon containing all poinst in S

Divide and conquer strategy to find the convex hull
O(n^2) complexity
"""


def tangent(i, j, mid):
    # y = mx + c
    m = (j[1] - i[1]) / (j[0] - i[0])
    return m * mid


def convex_hull(points):
    """
    @params:
        points: list of coordinates (x, y)
        e.g. [(1, 2), (4, 2), (5, 6), (3, 1), (9, 8), (7, 4)]
    @returns:
        list of points on the convex hull
        e.g. [(1, 2), (4, 2), (5, 6), (3, 1)]
    """

    # Base case
    if len(points) <= 3:
        return points

    # Sort points by x coordinate
    points = sorted(points, key=lambda point: point[0])

    # Separate into two parts
    mid = len(points) // 2
    left, right = points[:mid], points[mid:]

    # Get the convex hull of each part
    left_hull = convex_hull(left)
    right_hull = convex_hull(right)

    upper_tangent = lower_tangent = None

    # Merge the two hulls
    i, j = -1, 0
    left_last = left_hull[-1][0]
    right_first = right_hull[0][0]
    mid_x = left_last + (right_first - left_last)
    while (tangent(left_hull[i], right_hull[j+1], mid_x) > tangent(left_hull[i], right_hull[j], mid_x)) or \
            (tangent(left_hull[i-1], right_hull[j], mid_x) > tangent(left_hull[i], right_hull[j], mid_x)):
        if tangent(left_hull[i], right_hull[j+1], mid_x) > tangent(left_hull[i], right_hull[j], mid_x):
            j += 1
        else:
            i -= 1
    upper_tangent = [left_hull[i], right_hull[j]]
