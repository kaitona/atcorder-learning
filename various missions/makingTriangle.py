import sys

def solve(pollCount, polls):
    hashmap = {}
    for poll in polls:
        if poll not in hashmap: hashmap[poll] = 1
    polls = list(hashmap.keys())
    polls.sort(reverse = True)
    for i in range(len(polls)-2):
        for j in range(i+1, len(polls)-1):
            pass

    

data = sys.stdin.readlines()
pollCount = int(data[0].replace("\n", ""))
polls = list(map(int, data[1].split(" ")))

solve(pollCount, polls)