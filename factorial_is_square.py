#!/usr/bin/python3

import sympy
import math
import collections

"""Testing hypothesis if there is a factorial which is a square number

Detailed testing of this hypotheis:
for natural n > 1 extist natural o so n! = o^2
To fulfill the hypothesis the number n! must have even number of its every
factor. The program counts factors with odd number.
"""

# TODO:
# rewrite as a generator

def main():
    maxn = 1000000
    nplaces = math.floor(math.log10(maxn)) + 1
    nfacfac = collections.Counter()

    for n in range(2, maxn):
        nfac = sympy.ntheory.factorint(n)
        nfacfac += nfac
        oddf = 0    # odd numbered factors
        for fac in nfacfac:
            if nfacfac[fac] % 2: oddf += 1
        if oddf < 4:
            print(f"{n: {nplaces}} {oddf}")

if __name__ == "__main__":
    main()
