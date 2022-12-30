import sys

def solve(numOfCards, cards):
    winner = 0
    loser = 0
    
    cards.sort(reverse=True)

    for i in range(numOfCards):
        if i % 2 == 0: winner += cards[i]
        else: loser += cards[i]

    print(winner-loser)
    

data = sys.stdin.readlines()
numOfCards = int(data[0].replace(" ", ""))
cards = list(map(int, data[1].split(" ")))

solve(numOfCards, cards)