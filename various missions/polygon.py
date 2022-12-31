import sys

def solve(count, lines):
    print(solveHelper(count, lines))

def solveHelper(count, lines):
    lines.sort(reverse = True)
    longest = lines[0]
    for i in range(1,count):
        longest -= lines[i]
        if longest < 0: return "Yes"
    return "No"

data = sys.stdin.readlines()
lineCount = int(data[0].replace("\n", ""))
lines = list(map(int, data[1].split(" ")))

solve(lineCount, lines)