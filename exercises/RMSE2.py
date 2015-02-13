#!/usr/bin/env python3

# --------
# RMSE2.py
# --------

from functools import reduce
from math      import sqrt
from numpy     import mean, sqrt, square, subtract
from sys       import version
from timeit    import timeit

def rmse_while (a, p) :
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

def rmse_range_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__getitem__"))
    assert(hasattr(p, "__getitem__"))
    v = 0
    for i in range(len(a)) :
        v += (a[i] - p[i]) ** 2
    return sqrt(v / len(a))

def rmse_zip_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    z = zip(a, p)
    v = 0
    for x, y in z :
        v += (x - y) ** 2
    return sqrt(v / len(a))

def rmse_zip_reduce (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    z = zip(a, p)
    v = reduce(lambda v, a : v + (a[0] - a[1]) ** 2, z, 0)
    return sqrt(v / len(a))

def rmse_map_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    v = sum(map(lambda x, y : (x - y) ** 2, a, p))
    return sqrt(v / len(a))

def rmse_zip_list_sum (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z])
    return sqrt(v / len(a))

def rmse_zip_generator_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)
    return sqrt(v / len(a))

def rmse_numpy (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    return sqrt(mean(square(subtract(a, p))))

def test (f) :
    print(f.__name__)
    assert f((2, 3, 4), (2, 3, 4)) == 0
    assert f((2, 3, 4), (3, 2, 5)) == 1
    assert f((2, 3, 4), (4, 1, 6)) == 2
    assert f((2, 3, 4), (4, 3, 2)) == 1.632993161855452
    t = timeit("assert " + f.__name__ + "(10000 * [1], 10000 * [5]) == 4", "from __main__ import " + f.__name__, number = 100)
    print("{:.2f} milliseconds".format(t * 1000))
    print()

print("RMSE2.py")
print()

print(version)
print()

test(rmse_while)
test(rmse_range_for)
test(rmse_zip_for)
test(rmse_zip_reduce)
test(rmse_map_sum)
test(rmse_zip_list_sum)
test(rmse_zip_generator_sum)
test(rmse_numpy)

print("Done.")

"""
rmse.py

3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]

rmse_while
1393.41 milliseconds

rmse_range_for
1268.21 milliseconds

rmse_zip_for
924.56 milliseconds

rmse_zip_reduce
1246.97 milliseconds

rmse_map_sum
1019.86 milliseconds

rmse_zip_list_sum
891.52 milliseconds

rmse_zip_generator_sum
910.61 milliseconds

rmse_numpy
325.95 milliseconds

Done.
"""
