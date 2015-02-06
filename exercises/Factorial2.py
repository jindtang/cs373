#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

# https://docs.python.org/3.4/library/math.html

from functools import reduce
from math      import factorial
from operator  import mul
from sys       import version
from timeit    import timeit

# recursive procedure
# linear recursive process
def factorial_recursion (n) :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
def factorial_tail_recursion (n) :
    assert n >= 0
    def f (n, v) :
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)
    return f(n, 1)

# iterative procedure
# linear iterative process
def factorial_while (n) :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_range_for (n) :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_range_reduce (n) :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)

def test (f) :
    print(f.__name__)
    assert f(0) ==   1
    assert f(1) ==   1
    assert f(2) ==   2
    assert f(3) ==   6
    assert f(4) ==  24
    assert f(5) == 120
    t = timeit(f.__name__ + "(100)", "from __main__ import " + f.__name__, number = 1000)
    print("{:.2f} milliseconds".format(t * 1000))
    print()

print("Factorial.py")
print()

print(version)
print()

test(factorial_recursion)
test(factorial_tail_recursion)
test(factorial_while)
test(factorial_range_for)
test(factorial_range_reduce)
test(factorial)

print("Done.")

"""
Factorial.py

3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]

factorial_recursion
19.50 milliseconds

factorial_tail_recursion
25.03 milliseconds

factorial_while
12.65 milliseconds

factorial_range_for
7.63 milliseconds

factorial_range_reduce
7.67 milliseconds

factorial
1.12 milliseconds

Done.
"""
