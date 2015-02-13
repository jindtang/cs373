#!/usr/bin/env python3

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.4/library/functools.html

from operator import add, mul, sub
from unittest import main, TestCase

def reduce (bf, a, v) :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        assert reduce(add, [],                  0)  == 0

    def test_2 (self) :
        assert reduce(add, [2, 3, 4],           0)  ==  9

    def test_3 (self) :
        assert reduce(sub, [2, 3, 4],           0)  == -9

    def test_4 (self) :
        assert reduce(mul, [2, 3, 4],           1)  == 24

    def test_5 (self) :
        assert reduce(add, ([2, 3, 4], [5, 6]), []) == [2, 3, 4, 5, 6]

    def test_6 (self) :
        assert reduce(add, [(2, 3, 4), (5, 6)], ()) == (2, 3, 4, 5, 6)

    def test_7 (self) :
        assert reduce(add, ("abc",     "de"),   "") == "abcde"

if __name__ == "__main__" :
    main()
