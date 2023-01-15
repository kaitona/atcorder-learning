import sys
def solve(height, width, grid, opeCount, ope):
    for i in range(opeCount):
        grid = solveHelper(height, width, grid, ope[i])
    for row in grid:
        print("".join(row))
        
    

def solveHelper(height, width, grid, ope):
    tempGrid = [["0" for i in range(width)] for i in range(height)]
    heightGrid = height - int(ope[0])
    widthGrid = width - int(ope[1])
    for i in range(int(ope[0])):
        for j in range(int(ope[1])):
            tempGrid[int(ope[0])-1-i][int(ope[1])-1-j] = grid[i][j]
    for i in range(int(ope[0]), height):
        for j in range(int(ope[1]), width):
            tempGrid[height-i-1+int(ope[0])][width-j-1+int(ope[1])] = grid[i][j]
    for i in range(int(ope[0]), height):
        for j in range(int(ope[1])):
            tempGrid[height-i-1+int(ope[0])][int(ope[1])-1-j] = grid[i][j]
    for i in range(int(ope[0])):
        for j in range(int(ope[1]), width):
            tempGrid[int(ope[0])-1-i][width-j-1+int(ope[1])] = grid[i][j]
    
    grid = tempGrid
    return grid
    

data = sys.stdin.readlines()
data = [data[i].replace("\n", "") for i in range(len(data))]
gridData = data[0].split(" ")
height = int(gridData[0])
width = int(gridData[1])
grid = [list(data[i]) for i in range(1, 1+height)]
opeCount = int(data[height+1])
ope = [data[i].split(" ") for i in range(height+2, len(data))]
solve(height, width, grid, opeCount, ope)



