def solve(count,money):
    billList = solveHelper(count, money)
    print(billList[0],billList[1],billList[2])

def solveHelper(count, money):
    truth = False
    for i in range(count+1):
        for j in range(count+1-i):
            k = count - i - j
            if (10000*i+5000*j+1000*k) == money: return [i, j, k]

    return [-1, -1, -1]


data = list(map(int, input().split(" ")))
billCount = data[0]
totalMoney = data[1]

solve(billCount, totalMoney)