#!/usr/bin/env python3

# -------
# RMSE.py
# -------

from math     import sqrt
from unittest import main, TestCase

def rmse (a, p) :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(rmse([2, 3, 4], [2, 3, 4]), 0)

    def test_2 (self) :
        self.assertEqual(rmse([2, 3, 4], [3, 2, 5]), 1)

    def test_3 (self) :
        self.assertEqual(rmse([2, 3, 4], [4, 1, 6]), 2)

    def test_4 (self) :
        self.assertEqual(rmse([2, 3, 4], [4, 3, 2]), 1.632993161855452)

if __name__ == "__main__" :
    main()
