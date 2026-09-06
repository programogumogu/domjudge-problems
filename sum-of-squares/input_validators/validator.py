#!/usr/bin/env python3
import sys

data = sys.stdin.read().strip().split()
if len(data) < 2:
    sys.exit(1)

try:
    N = int(data[0])
except:
    sys.exit(1)

if N <= 0:
    sys.exit(1)

if len(data[1:]) != N:
    sys.exit(1)

for x in data[1:]:
    try:
        int(x)
    except:
        sys.exit(1)

sys.exit(0)
