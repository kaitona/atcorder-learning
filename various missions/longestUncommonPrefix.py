import sys

def solve(N, string):
    for i in range(1,N):
        l = 0
        for j in range(1, N-i+1):
            if string[j-1] != string[j+i-1]:
                l += 1
            else: break
        print(l)


data = sys.stdin.readlines()
N = int(data[0])
string = list(data[1].replace("\n", ""))
solve(N, string)
