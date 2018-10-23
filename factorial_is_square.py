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
# get rid of global variables
# convert to object?
# read CLI parameters

start = 2
maxn = 100
nplaces = math.floor(math.log10(maxn)) + 1

def nfacfac(start=1):
    """generate factors of n! starting from start

    This is a generator which returns prime factors of n!
    starting from specified n or 1.
    The factors are represented by the Counter class."""
    result = collections.Counter()
    if start > 2:
        result += sympy.ntheory.factorint(math.factorial(n-1))
    # internal factors variable initialized
    for n in itertools.count(start):
        result += sympy.ntheory.factorint(n)
        yield result

def counter_count_odd(counter):
    """count number of odd numbered items

    Could be used for example to cound odd numbered prime factors
    which prevent the number to be a perfect square."""
    oddn = 0
    for item in counter:
        if counter[item] % 2:
            oddn += 1
    return oddn

def main():
    for n, facfac in enumerate(itertools.islice(nfacfac(start), maxn), start=start):
        oddf = counter_count_odd(facfac)
        if oddf < 4:
            print(f"{n: {nplaces}} {oddf}")

if __name__ == "__main__":
    main()
