import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(map, start, seen):
    seen[start[0]][start[1]] = True

    for i in range(len(dx)):
        nh = start[0] + dx[i]
        nw = start[1] + dy[i]
        if nh < 0 or nh >= 10 or nw < 0 or nw >= 10: continue
        if map[nh][nw] == "x": continue
        if seen[nh][nw]: continue
        dfs(map, [nh, nw], seen)

data = sys.stdin.readlines()
seen = [[False for _ in range(10)] for _ in range(10)]
landing = [list(data[i].replace("\n", "")) for i in range(10)]
def solve(landing, seen):
    for i in range(10):
        for j in range(10):
            currentIndex = landing[i][j]
            landing[i][j] = "o"
            total = 0
            if seen[i][j] == True: continue
            if seen[i][j] == False and landing[i][j] == "x": 
                continue
            dfs(landing, [i, j], seen)
            for n in range(10):
                for m in range(10):
                    if (seen[n][m] == False and landing[n][m] == "x") or (seen[n][m] == True and landing[n][m] == "o"): total += 1
            if total == 100: 
                return "YES"
            seen = [[False for _ in range(10)] for _ in range(10)]
            landing[i][j] = currentIndex
    return "NO"


print(solve(landing, seen))