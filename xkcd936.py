#!/usr/bin/env python3
"""Quick implementation of XKCD 936."""
import random
import sys


def xkcd936(length):
    """Quick implementation of XKCD 936."""
    with open('/usr/share/dict/words') as f:
        words = [line.strip() for line in f.readlines()]

    words = [w for w in words if "'" not in w]

    for _ in range(0, length):
        print(random.choice(words).capitalize(), end='')

    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    else:
        length = 3

    xkcd936(length)
