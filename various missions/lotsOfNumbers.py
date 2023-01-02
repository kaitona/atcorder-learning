def solve(num):
    opeIndexCount = len(num) - 1
    bits = []
    for i in range(2**opeIndexCount):
        bits.append("0"*(opeIndexCount - len(bin(i)[2:]))+bin(i)[2:])
    result = 0
    for binary in bits:
        sum = 0
        plusIndex = 0
        for i in range(len(binary)):
            if binary[i] == "1":
                sum += int(num[plusIndex:i+1])
                plusIndex = i+1
            if len(binary)-1 == i:
                sum += int(num[plusIndex:])
                plusIndex = 0
        result += sum
    print(result)
            
num = input()
solve(num)