import sys

def solve(numCount, numList):
    count = 0
    includeOdd = False
    while not includeOdd:
        for i in range(numCount):
            if numList[i] % 2 == 1:
                print(count)
                includeOdd = True
                break
        count += 1
        for i in range(numCount):
            numList[i] /= 2

data = sys.stdin.readlines()
numCount = int(data[0].replace(" ",""))
numList = list(map(int, data[1].split(" ")))
solve(numCount, numList)
    