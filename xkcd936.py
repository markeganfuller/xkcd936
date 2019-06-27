#!/usr/bin/env python3
import random
import sys


with open('/usr/share/dict/words') as f:
    words = [l.strip() for l in f.readlines()]

words = [w for w in words if "'" not in w]

for i in range(0, int(sys.argv[1])):
    print(random.choice(words).capitalize(), end='')

print()
