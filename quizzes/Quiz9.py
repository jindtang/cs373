#!/usr/bin/env python3

"""
CS373: Quiz #9 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. Which of the following practices demonstrates effective pair
    programming?
    [All I Really Needed to Know about Pair Programming I Learned in
     Kindergarten]
    (2 pts)

a. Each partner writing separate parts.
b. Each partner writing both parts and then submitting the best.
c. Each partner writing both parts and then submitting the best
   combination.
d. Sharing a monitor and keyboard while coding.
e. One partner writing the interface and tests, the other the
   implementation.

d.
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (4 pts)

0.0
1.0
2.0
1.632993161855452
"""

from math import sqrt

def rmse (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__getitem__"))
    assert(hasattr(p, "__getitem__"))
    i = 0
    v = 0
    while i != len(a) :
        v += (a[i] - p[i]) ** 2
        i += 1
    return sqrt(v / len(a))

print(rmse([2, 3, 4], [2, 3, 4]))
print(rmse([2, 3, 4], [3, 2, 5]))
print(rmse([2, 3, 4], [4, 1, 6]))
print(rmse([2, 3, 4], [4, 3, 2]))
