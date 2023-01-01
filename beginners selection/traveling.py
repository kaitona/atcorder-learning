import sys

def solve(count, plans):
    print(solveHelper(count, plans))

def solveHelper(count, plans):
    defaultPosition = [0, 0, 0]
    for i in range(count):
        elapsedTime = plans[i][0] - defaultPosition[0]
        horizontal = plans[i][1] - defaultPosition[1]
        vertical = plans[i][2] - defaultPosition[2]

        if vertical == 0: 
            if not(abs(horizontal) <= elapsedTime and abs(horizontal) % 2 == elapsedTime % 2): return "No" 
        elif horizontal == 0:
            if not(abs(vertical) <= elapsedTime and abs(vertical) % 2 == elapsedTime % 2): return "No"
        else:
            if not(abs(vertical)+abs(horizontal) <= elapsedTime and (abs(vertical)+abs(horizontal))%2 == elapsedTime % 2): return "No"
        defaultPosition = [plans[i][0], plans[i][1], plans[i][2]]
    return "Yes"

data = sys.stdin.readlines()
planCount = int(data[0].replace("\n", ""))
plans = []
for i in range(1, planCount+1):
    plans.append(list(map(int, data[i].split(" "))))

solve(planCount, plans)