#!/usr/bin/env python3

# ------------
# Coverage3.py
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

    def test_3 (self) :
        self.assertEqual(cycle_length(3), 8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% Coverage3.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK



% coverage3 run --branch Coverage3.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK



% coverage3 report -m
Name        Stmts   Miss Branch BrMiss  Cover   Missing
-------------------------------------------------------
Coverage3      19      0      4      0   100%
"""
