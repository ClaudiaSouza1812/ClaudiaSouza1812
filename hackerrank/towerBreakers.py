import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# my solution
def towerBreakers(n, m):
    # Write your code here
    p1 = True
    p2 = False
    scr1 = 0
    scr2 = 0
    r = n % 2
    heights = []

    for i in range(n):
        heights.append(m)

    while any(n != 1 for n in heights):
        if p1:
            index = heights.index(max(heights))
            h = heights[index]
            y = h - 1

            while h % y != r:
                y -= 1

            heights[index] = h - y
            p1 = False
            p2 = True
            scr1 += 1
        elif p2:
            index = heights.index(max(heights))
            h = heights[index]
            y = h - 1

            while h % y != r:
                y -= 1
            heights[index] = h - y
            p1 = True
            p2 = False
            scr2 += 1

    if scr1 > scr2:
        return 1
    else:
        return 2



# web solution:
def towerBreakers(n, m):
    # Write your code here
    if m== 1 or n%2 ==0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
