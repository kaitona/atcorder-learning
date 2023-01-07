import sys
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def searchGoalOrStart(height, width, map, string):
    if string == "start":
        for i in range(height):
            for j in range(width):
                if map[i][j] == "s": return [i, j]
    else:
        for i in range(height):
            for j in range(width):
                if map[i][j] == "g": return [i, j]


def dfs(map, height, width, seen, currentIndex):
    h = currentIndex[0]
    w = currentIndex[1]
    seen[h][w] = True

    for i in range(len(dx)):
        nh = h + dx[i]
        nw = w + dy[i]
        if nh < 0 or nh >= height or nw < 0 or nw >= width: continue
        if map[nh][nw] == "#": continue
        if seen[nh][nw]: continue
        dfs(map, height, width, seen, [nh,nw])

data = sys.stdin.readlines()
height = int(data[0].split(" ")[0])
width = int(data[0].split(" ")[1])
map = [list(data[i].replace("\n", "")) for i in range(1,height+1)]
seen = [[False for _ in range(width)] for _ in range(height)]

start = searchGoalOrStart(height, width, map, "start")
goal = searchGoalOrStart(height, width, map, "goal")


dfs(map, height, width, seen, start)

if seen[goal[0]][goal[1]]: print("Yes")
else: print("No")

