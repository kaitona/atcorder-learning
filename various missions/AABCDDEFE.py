import sys

def solve(index):
    numList = []
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                for n in range(10):
                    for m in range(10):
                        for f in range(10):
                            num = [0,0,0,0,0,0,0,0,0]
                            num[0] = str(i)
                            num[1] = str(i)
                            num[2] = str(j)
                            num[3] = str(k)
                            num[4] = str(n)
                            num[5] = str(n)
                            num[6] = str(m)
                            num[7] = str(f)
                            num[8] = str(m)
                            num = int("".join(num))
                            numList.append(num)
    numList.sort()
    print(numList[index-1])

index = int(sys.stdin.readlines()[0])
solve(index)
