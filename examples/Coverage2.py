#!/usr/bin/env python3

# ------------
# Coverage2.py
# ------------

# https://pypi.python.org/pypi/coverage/3.7.1

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length(1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length(2), 2)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% Coverage2.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK



% coverage3 run --branch Coverage2.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK



% coverage3 report -m
Name        Stmts   Miss Branch BrMiss  Cover   Missing
-------------------------------------------------------
Coverage2      17      1      4      1    90%   18
"""
