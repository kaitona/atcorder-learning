import sys

def solve(count, arr):
    hashmap = {}
    for num in arr:
        if num not in hashmap: hashmap[num] = 1
    print(len(hashmap))
    


data = sys.stdin.readlines()
mochiCount = int(data[0].replace(" ", ""))
mocheis = [int(data[i].replace("\n", "")) for i in range(1,mochiCount+1)]

solve(mochiCount, mocheis)