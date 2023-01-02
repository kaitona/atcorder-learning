def solve(num):
    for i in range(2 ** (len(num)-1)):
        combi = ""
        for j in range(len(num)-1):
            if((i >> j) & 1): combi += num[j] + "+"
            else: combi += num[j] + "-"
        combi += num[len(num)-1]
        if eval(combi) == 7:
            print(combi + "=7")
            break

num = list(input())
solve(num)