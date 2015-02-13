#!/usr/bin/env python3

# -------
# Map2.py
# -------

# https://docs.python.org/3.4/library/functions.html#map

from unittest import TestCase, TestLoader, TestSuite, TextTestRunner

def map_for_range (uf, a) :
    for i in range(len(a)) :
        yield uf(a[i])

def map_while (uf, a) :
    p = iter(a)
    try :
        while True :
            yield uf(next(p))
    except StopIteration :
        pass

def map_for (uf, a) :
    for v in a :
        yield uf(v)

def map_generator (uf, a) :
    return (uf(v) for v in a)

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            a = ()
            assert list(f(lambda x : x ** 2, a)) == []

        def test_2 (self) :
            a = (2, 3, 4)
            assert list(f(lambda x : x ** 2, a)) == [4,  9, 16]

        def test_3 (self) :
            a = ([2], [3], [4])
            assert list(f(lambda x : x + [5], a)) == [[2, 5], [3, 5], [4, 5]]

        def test_4 (self) :
            a = ("abc", "def", "ghi")
            assert list(f(lambda x : x + "xyz", a)) == ["abcxyz", "defxyz", "ghixyz"]
    return MyUnitTests

if __name__ == "__main__" :
    s = TestSuite()
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map_for_range)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map_while)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map_for)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map_generator)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map)))
    TextTestRunner().run(s)
