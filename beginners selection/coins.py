import sys

def solve(num1, num2, num3, total):
    result = 0

    for i in range(num1+1):
        for j in range(num2+1):
            for k in range(num3+1):
                if (500 * i + 100 * j + 50 * k) == total: result += 1

    print(result)

data = sys.stdin.readlines()
fiveHundred = int(data[0].replace(" ", ""))
fifty = int(data[1].replace(" ", ""))
ten = int(data[2].replace(" ", ""))
totalMoney = int(data[3].replace(" ", ""))

solve(fiveHundred, fifty, ten, totalMoney)