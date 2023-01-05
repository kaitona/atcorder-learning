def solve(num, numList):
    for i in range(len(numList)):
        if num == numList[i]: return len(numList)+1
    numList.append(num)

    if num % 2 ==0: return solve(num/2, numList)
    else: return solve(3*num+1, numList)


num = int(input())
numList = []
print(solve(num, numList))