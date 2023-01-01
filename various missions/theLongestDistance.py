import sys
import math

def solve(count, points):
    max = 0
    currentPoint = points[0]
    for i in range(1, count):
        for j in range(i, count):
            distance = math.sqrt(math.pow(currentPoint[0]-points[j][0], 2)+math.pow(currentPoint[1]-points[j][1], 2))
            if max < distance: max = distance
        currentPoint = points[i]
    print(max)
            


data = sys.stdin.readlines()
pointCount = int(data[0].replace("\n", ""))
points = [list(map(int, data[i].split(" "))) for i in range(1,pointCount+1)]

solve(pointCount, points)