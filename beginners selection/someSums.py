import math

def solve(data):
    numRange = data[0]
    minSum = data[1]
    maxSum = data[2]
    result = 0

    for i in range(1,numRange+1):
        if digitSum(i) >= minSum and digitSum(i) <= maxSum: result += i
    
    print(result)

def digitSum(num):
    total = 0
    while num > 0:
        total += num % 10
        num = math.floor(num/10)

    return total

    

data = list(map(int, input().split(" ")))
solve(data)
