import sys
import math

def solve(meats):
    result = math.inf
    for i in range(2 ** len(meats)):
        timeLow = 0
        timeHigh = 0
        for j in range(len(meats)):
            if((i >> j) & 1): timeLow += meats[j]
            else: timeHigh += meats[j]
        if timeHigh < timeLow: timeHigh = timeLow
        if result > timeHigh: result = timeHigh
    print(result)

data = sys.stdin.readlines()
meats = [int(data[i].replace("\n", "")) for i in range(1, len(data))]
solve(meats)