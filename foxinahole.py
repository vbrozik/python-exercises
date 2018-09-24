#!/usr/bin/python3



import msvcrt
import itertools
import argparse

"""foxinahole puzzle manual and automated solver

The script aids to solve or solves by itself the fox in a hole puzzle
or special case of more generic princess on a graph puzzle:
  * https://gurmeet.net/puzzles/fox-in-a-hole/
  * https://www.checkmyworking.com/2011/12/solving-the-princess-on-a-graph-puzzle/

The script can be run in two modes. By default it runs manual interactive mode
where you can try to solve the puzzle by inspecting a hole in steps or you can
run the automatic solver.
"""

def reprfox(present):
    return '+' if present else '-'

def reprholes(foxinhole):
    repr = ''
    for hole in foxinhole:
        repr += (' ' if repr else '') + reprfox(hole)
    return repr

def itemornone(lst, idx):
    slst = lst[idx:idx+1]
    return slst[0] if slst else None

def checkandmove(foxinhole, holechecked):
    # foxinhole2 = [None] * len(foxinhole)
    foxinhole2 = []
    foxinhole[holechecked] = False
    # print(foxinhole, holechecked)
    for pos in range(len(foxinhole)):
        foxinhole2.append(itemornone(foxinhole, pos - 1) or
                          itemornone(foxinhole, pos + 1))
    return foxinhole2[:]

def interactive(nholes):
    day = 1
    foxinhole = [True] * nholes
    while True:
        # print possible fox positions
        print(f"{day:2d}   {reprholes(foxinhole)}")
        if not any(foxinhole):
            break
        # check a hole and move the fox
        while True:
            keypress = msvcrt.getwch()
            if keypress in {'q', 'Q'}: return
            holechecked = ord(keypress) - ord('1')
            if 0 <= holechecked < nholes:
                break
        print(f"""     {" "*holechecked*2}^""")
        foxinhole = checkandmove(foxinhole, holechecked)
        day += 1
    print("\nCongratulations you have caught the smartest fox!")

def automatic(nholes, maxsteps):
    for iseq, seq in enumerate(itertools.product(range(nholes), repeat=maxsteps)):
        if not iseq & 4095:
            print(seq, '\r', end='')
        foxinhole = [True] * nholes
        for idx, holechecked in enumerate(seq):
            foxinhole = checkandmove(foxinhole, holechecked)
            if not any(foxinhole):
                print(f"{seq[:idx+1]!s:<20}   {reprholes(foxinhole)}")
                break

def main():
    parser = argparse.ArgumentParser(description="Solve fox in a hole puzzle")
    parser.add_argument('nholes', type=int, nargs='?', default=5,
                        help='number of holes (1 - 9)')
    parser.add_argument('msteps', type=int, nargs='?', default=6,
                        help='max number of steps for automatic solving')
    parser.add_argument('--auto', dest='automatic', action='store_true',
                        help='solve the puzzle automatically')
    args = parser.parse_args()
    if args.automatic:
        automatic(args.nholes, args.msteps)
    else:
        interactive(args.nholes)

if __name__ == "__main__":
    main()
