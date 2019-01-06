from typing import List


def mod(x: int, m: int):
    r: int = x % m
    return r + m if r < 0 else r


players: List[int] = [0 for x in range(471)]
currentPlayer = 0
maximumMarbleValue = 72026
marbles = [0]
currentMarble = 0

for marbleValue in range(1, maximumMarbleValue + 1):
    if marbleValue % 23 == 0:
        players[currentPlayer] += marbleValue
        popIndex = mod((currentMarble - 7), len(marbles))
        players[currentPlayer] += marbles.pop(popIndex)
        currentMarble = popIndex
        currentPlayer = (currentPlayer + 1) % len(players)
        continue

    insertPoint = (currentMarble + 2) % len(marbles)
    if insertPoint == 0 or insertPoint >= len(marbles):
        marbles.append(marbleValue)
        currentMarble = len(marbles) - 1
    else:
        marbles.insert(insertPoint, marbleValue)
        currentMarble = insertPoint
    currentPlayer = (currentPlayer + 1) % len(players)

print(max(players))
