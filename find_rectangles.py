#!/usr/bin/python3

""" Find all possible rectangles from given 2-coordinate points.
Google Coding Interview With A Competitive Programmer
https://www.youtube.com/watch?v=EuPSibuIKIg
"""

from __future__ import annotations

import random
from typing import Iterable, Hashable, Sequence

points1 = [
    (1,1),
    (2,1),
    (3,1),
    (1,2),
    (2,2),
    (3,2)
]

def points_to_dicts(points: Iterable[Sequence[Hashable]]) -> (
                        tuple[dict[Hashable, set[Hashable]],
                                dict[Hashable, set[Hashable]]]):
    x_dict: dict[Hashable, set[Hashable]] = {}
    y_dict: dict[Hashable, set[Hashable]] = {}
    for x, y in points:
        if x not in x_dict:
            x_dict[x] = set()
        x_dict[x].add(y)
        if y not in y_dict:
            y_dict[y] = set()
        y_dict[y].add(x)
    return x_dict, y_dict

def get_rectangles(point: tuple, dicts: tuple) -> list:
    rectangles = []
    if len(dicts[0][point[0]]) < 2:
        return rectangles
    return rectangles

def main():
    random.shuffle(points1)
    points1.sort()
    print(points_to_dicts(points1))

if __name__ == '__main__':
    main()
