def solve(num, numList):
    return solveHelper(num, numList)

def solveHelper(num, numList):
    for i in range(len(numList)):
        if num == numList[i]:
            print(len(numList)+1)
            return True
    numList.append(num)

    if num % 2 ==0: solveHelper(num/2, numList)
    else: solveHelper(3*num+1, numList)


num = int(input())
numList = []
solve(num, numList)