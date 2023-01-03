
import math
import os
import random
import re
import sys

#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
def getMaxScore(jewels):
    # Initialize a dictionary to store the count of each type of jewel
    jewel_count = {}
    for jewel in jewels:
        if jewel not in jewel_count:
            jewel_count[jewel] = 0
        jewel_count[jewel] += 1

    # Initialize the maximum score to 0
    max_score = 0

    # Iterate through the string and update the maximum score
    for jewel, count in jewel_count.items():
        max_score += count // 2

    return max_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        jewels = input()

        ans = getMaxScore(jewels)

        fptr.write(str(ans) + '\n')

    fptr.close()
