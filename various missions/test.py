def solve(num):
    result = 0
    combinations = []
    for i in range(2 ** (len(num)-1)):
        combi=""
        for j in range(len(num)-1):
            if((i >> j)&1): combi += num[j] + "+"
            else: combi += num[j] + ""
        combi += num[len(num)-1]
        combinations.append(combi)
    
    for combi in combinations:
        result += eval(combi)
    print(result)


num = list(input())
solve(num)