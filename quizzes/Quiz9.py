#!/usr/bin/env python3

"""
CS373: Quiz #9 (7 pts)
"""

""" ----------------------------------------------------------------------
 1. Which of the following practices demonstrates effective pair
    programming?
    [All I Really Needed to Know about Pair Programming I Learned in
     Kindergarten]
    (3 pts)

a. Each partner writing separate parts.
b. Each partner writing both parts and then submitting the best.
c. Each partner writing both parts and then submitting the best
   combination.
d. Sharing a monitor and keyboard while coding.
e. One partner writing the interface and tests, the other the
   implementation.

d.
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (6 pts)

g1 f1 f2 g2 else finally g3
g1 f1 except finally g3
g1 f1 finally
"""

def f (n) :
    print("f1", end = " ")
    if n == 1 :
        raise KeyError()
    elif n == 2:
        raise TypeError()
    print("f2", end = " ")

def g (n) :
    try :
        print("g1", end = " ")
        f(n)
        print("g2", end = " ")
    except KeyError :
        print("except", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")
    print("g3")

try :
    for n in [0, 1, 2] :
        g(n)
except Exception :
    print()
