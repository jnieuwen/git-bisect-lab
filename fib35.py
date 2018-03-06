#!/usr/bin/env python

import sys

if __name__ == '__main__':
    n = 35

    if n == 0:
        print(0)
        sys.exit()

    if n == 1:
        print("0,1")
        sys.exit()


    values = []
    values.append(0)
    values.append(1)



    while len(values) <= n:
        values.append(values[-1] + values[-2])

    print(",".join(map(str,values)))



