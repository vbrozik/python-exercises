#!/usr/bin/python3

import sympy
import math
import collections
import itertools

"""Testing hypothesis if there is a factorial which is a square number

Detailed description of the testing:
for a natural n > 1 extist a natural o so n! = o^2
To fulfill the hypothesis the number n! must have even number of its every
factor. The program counts factors with odd number.
"""

# TODO:

maxn = 100
nplaces = math.floor(math.log10(maxn)) + 1

def nfacfac(start=1):
    """factors of n! starting from start"""
    result = collections.Counter()
    if start > 2:
        result += sympy.ntheory.factorint(math.factorial(n-1))
    for n in itertools.count(start):
        result += sympy.ntheory.factorint(n)
        yield result

def main():
    for n, facfac in enumerate(itertools.islice(nfacfac(2), maxn)):
        oddf = 0    # odd numbered factors
        for fac in facfac:
            if facfac[fac] % 2: oddf += 1
        if oddf < 4:
            print(f"{n: {nplaces}} {oddf}")

if __name__ == "__main__":
    main()
