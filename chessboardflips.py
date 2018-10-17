#!/usr/bin/python3

""" puzzle to turn chessboard single color by flipping both columns and rows
"""

# UNFINISHED

import msvcrt

def chessboard_init(size=8):
    return [[bool((row + col) % 2)
                    for col in range(size)] for row in range(size)]

def chessboard_show(chessboard):
    for row in chessboard:
        for item in row:
            print('#' if item else ' ', end='')
        print()

def chessboard_flip_col(chessboard, col):
    for row, _item in (item[col] for item in chessboard):
        # TypeError: cannot unpack non-iterable bool object
        chessboard[col][row] = not chessboard[col][row]

def chessboard_flip_row(chessboard, row):
    for col, _item in enumerate(chessboard[row]):
        chessboard[col][row] = not chessboard[col][row]

def interactive(chessboard, size=8):
    while True:
        chessboard_show(chessboard)
        while True:
            keypress = msvcrt.getwch()
            if keypress in {'q', 'Q'}: return
            rowcol = ord(keypress) - ord('1')
            if 0 <= rowcol < size:
                chessboard_flip_col(chessboard, rowcol)
                chessboard_flip_row(chessboard, rowcol)
                # for i in range(size):
                #     chessboard[rowcol][i] = not chessboard[rowcol][i]
                #     chessboard[i][rowcol] = not chessboard[i][rowcol]
                print()
                break
    return


def main():
    chessboard = chessboard_init()
    interactive(chessboard)

if __name__ == "__main__":
    main()
