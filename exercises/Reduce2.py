#!/usr/bin/env python3

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.4/library/functools.html

from functools import reduce
from operator  import add, mul, sub
from unittest  import TestCase, TestLoader, TestSuite, TextTestRunner

def reduce_for_range (bf, a, v) :
    for i in range(len(a)) :
        v = bf(v, a[i])
    return v

def reduce_while (bf, a, v) :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            assert f(add, [],                  0)  == 0

        def test_2 (self) :
            assert f(add, [2, 3, 4],           0)  ==  9

        def test_3 (self) :
            assert f(sub, [2, 3, 4],           0)  == -9

        def test_4 (self) :
            assert f(mul, [2, 3, 4],           1)  == 24

        def test_5 (self) :
            assert f(add, ([2, 3, 4], [5, 6]), []) == [2, 3, 4, 5, 6]

        def test_6 (self) :
            assert f(add, [(2, 3, 4), (5, 6)], ()) == (2, 3, 4, 5, 6)

        def test_7 (self) :
            assert f(add, ("abc",     "de"),   "") == "abcde"
    return MyUnitTests

if __name__ == "__main__" :
    s = TestSuite()
    s.addTest(TestLoader().loadTestsFromTestCase(bind(reduce_for_range)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(reduce_while)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(reduce_for)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(reduce)))
    TextTestRunner().run(s)
