def solve(numRange, total):
    count = 0
    for i in range(0, numRange+1):
        for j in range(0, numRange+1):
            if total-i-j >= 0 and total-i-j <= numRange: count += 1
    print(count)

data = list(map(int, input().split(" ")))
solve(data[0], data[1])