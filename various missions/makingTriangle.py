import sys

def solve(pollCount, polls):
    result = 0
    polls.sort(reverse = True)
    for i in range(len(polls)-2):
        for j in range(i+1, len(polls)-1):
            for k in range(j+1, len(polls)):
                if polls[j] + polls[k] > polls[i] and polls[i] != polls[j] and polls[j] != polls[k]: result += 1
    print(result)
            
data = sys.stdin.readlines()
pollCount = int(data[0].replace("\n", ""))
polls = list(map(int, data[1].split(" ")))

solve(pollCount, polls)