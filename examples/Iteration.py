#!/usr/bin/env python3

# -------------
# Indexables.py
# -------------

from itertools import count
from types     import GeneratorType

print("Iteration.py")

a = [2, 3, 4]
assert type(a) is list
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :
    s += v
assert s == 9

a = (2, 3, 4)
assert type(a) is tuple
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :
    s += v
assert s == 9

a = [2, 3, 4]
for v in a :
    v += 1            # ?
assert a == [2, 3, 4]

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"                      # ?
assert a == ["abc", "def", "ghi"]

a = [[2], [3], [4]]
for v in a :
    v += (5,)                        # ?
assert a == [[2, 5], [3, 5], [4, 5]]

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)                  # ?
assert a == [(2,), (3,), (4,)]

a = [[2, "abc"], [3, "def"], [4, "ghi"]]
s = 0
for u, v in a :
    s += u
assert s == 9

a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a :
    s += u
assert s == 9

a = {2, 3, 4}
assert type(a) is set
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :
    s += v
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
assert type(d) is dict
assert not hasattr(d, "__next__")
assert     hasattr(d, "__iter__")
s = 0
for k in d :
    s += k
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = ""
for k in d :
    s += d[k]
assert s == "abcdefghi"

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k, v in d.items() :
    s += k
assert s == 9

x = range(10)
assert type(x) is range
assert not hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
assert list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = range(2, 10)
assert list(x) == [2, 3, 4, 5, 6, 7, 8, 9]

x = range(2, 10, 2)
assert list(x) == [2, 4, 6, 8]

x = range(10, 2, -2)
assert list(x) == [10, 8, 6, 4]

x = range(10)
assert hasattr(x, "__getitem__")
assert x[0] == 0
assert x[9] == 9
try :
    assert x[10] == 10 # error: out of range
    assert False
except IndexError :
    pass
#x[0] = 2              # TypeError: 'xrange' object does not support item assignment
s = 0
for v in x :
    s += v
assert s == 45
s = 0
for v in x :
    s += v
assert s == 45

x = range(15)
s = 0
for v in x :
    if v == 10 :
        break
    s += v
else :           # else clause in a for loop
    assert False # executes when the loop terminates normally
assert s == 45

x = count(0)                         # 0, 1, 2, ...
assert type(x) is count
assert     hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
assert not hasattr(x, "__getitem__")
#assert (x[0] == 0)                  # TypeError: 'itertools.count' object is not indexable
s = 0
for v in x :
    if v == 10 :
        break
    s += v
assert s == 45
for v in x :
    if v == 20 :
        break
    s += v
assert s == 180

x = count(3, 2) # 3, 5, 7, 9, ...
s = 0
for v in x :
    if v > 10 :
        break
    s += v
assert s == 24

x = [2, 3, 4]
y = []
for v in x :
    y += [v * 5]
assert x == [ 2,  3,  4]
assert y == [10, 15, 20]

x = [2, 3, 4]
y = [v * 5 for v in x]            # list comprehension
assert type(y) is list
assert not hasattr(y, "__next__")
assert     hasattr(y, "__iter__")
assert x == [2,   3,  4]
assert y == [10, 15, 20]

x = [2, 3, 4]
y = map(lambda v : v * 5, x)
assert type(y) is map
assert hasattr(y, "__next__")
assert hasattr(y, "__iter__")
assert x       == [2,   3,  4]
assert list(y) == [10, 15, 20]
assert list(y) == []

x = [2, 3, 4]
y = map(lambda v : v * 5, x)
x += [5]
assert x       == [2,   3,  4,  5]
assert list(y) == [10, 15, 20, 25]
assert list(y) == []

x = [2, 3, 4]
y = (v * 5 for v in x)
assert type(y) is GeneratorType
assert hasattr(y, "__next__")
assert hasattr(y, "__iter__")
assert x       == [2,   3,  4]
assert list(y) == [10, 15, 20]
assert list(y) == []

x = [2, 3, 4]
y = (v * 5 for v in x)
x += [5]
assert x       == [ 2,  3,  4,  5]
assert list(y) == [10, 15, 20, 25]
assert list(y) == []

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
assert x == [2,  3,  4,  5,  6]
assert y == [   15,     25]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]
assert x == [ 2,  3,  4,  5,  6]
assert y == [    15,     25]

x = [2, 3, 4, 5, 6]
y = filter(lambda v : v % 2, x)
assert type(y) is filter
assert hasattr(y, "__next__")
assert hasattr(y, "__iter__")
z = map(lambda v : v * 5, y)
assert x       == [ 2,  3,  4,  5,  6]
assert list(z) == [    15,     25]

x = [2, 3, 4, 5, 6]
y = (v * 5 for v in x if v % 2)
assert x       == [ 2,  3,  4,  5,  6]
assert list(y) == [    15,     25]
assert list(y) == []

x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z += [v + w]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]

x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]

x = [2, 3, 4]
y = [4, 5]
z = (v + w for v in x for w in y)
assert x       == [2, 3, 4]
assert y       == [4, 5]
assert list(z) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert list(z) == []

x = {2, 3, 4}
y = set()
for v in x :
    y |= {v * 5}
assert x == { 2,  3,  4}
assert y == {10, 15, 20}

x = {2, 3, 4}
y = {v * 5 for v in x}   # set comprehension
assert x == { 2,  3,  4}
assert y == {10, 15, 20}

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {}
for k, v in x.items() :
    y[k] = v + "xyz"
assert x == {2 : "abc", 3 : "def", 4 : "ghi"}
assert y == {2 : "abcxyz", 3 : "defxyz", 4 : "ghixyz"}

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {k : v + "xyz" for k, v in x.items()}              # dict comprehension
assert type(y) is dict
assert not hasattr(y, "__next__")
assert     hasattr(y, "__iter__")
assert x == {2 : "abc", 3 : "def", 4 : "ghi"}
assert y == {2 : "abcxyz", 3 : "defxyz", 4 : "ghixyz"}

assert     all([True,  2, 3.45, "abc", [2, 3, 4], (2, 3, 4), {2, 3, 4}, {2 : "abc", 3 : "def", 4 : "ghi"}])
assert not any([False, 0, 0.0,  "",    [],        (),        set(),     dict()])

assert list(zip())                       == []
assert list(zip([]))                     == []
assert list(zip((), ()))                 == []
assert list(zip([2, 3]))                 == [(2,), (3,)]
assert list(zip((2, 3), (4, 5), (6, 7))) == [(2, 4, 6), (3, 5, 7)]
assert list(zip([2, 3, 4], [5, 6, 7]))   == [(2, 5), (3, 6), (4, 7)]

print("Done.")
