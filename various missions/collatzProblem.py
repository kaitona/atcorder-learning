def solve(num, numList):
    print(solveHelper(num, numList))

def solveHelper(num, numList):
    for i in range(len(numList)):
        if num == numList[i]:
            print(len(numList)+1)  
    numList.append(num)

    if num % 2 ==0: solveHelper(num/2, numList)
    if num % 2 ==1: solveHelper(3*num+1, numList)


num = int(input())
numList = []
solve(num, numList)