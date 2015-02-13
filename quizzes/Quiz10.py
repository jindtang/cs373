#!/usr/bin/env python3

"""
CS373: Quiz #10 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (6 pts)

9
1 4 9
1 4 9
generator # 3 pts
"""

from functools import reduce

print(reduce(lambda x, y : (x - y) ** 2, [2, 3, 4], 0))

for v in map(lambda x, y : (x - y) ** 2, [2, 3, 4], [3, 5, 7]) :
    print(v, end = " ")
print()

for v in [(x - y) ** 2 for x, y in zip([2, 3, 4], [3, 5, 7])] :
    print(v, end = " ")
print()

print(v for v in zip([2, 3, 4], [5, 6]))
