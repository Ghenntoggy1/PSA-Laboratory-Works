# 1. How much should I bet?:
import random

def coinflip():
    return random.choice(["Head", "Tail"])

listmw = []
x = 1
totmw = 0
games = int(input("Number of games: "))
for game in range(1, games + 1):
    mw = 0
    while True:
        coinflip()
        if coinflip() == "Tail":
            x += 1
        else:
            mw += 2 ** x
            totmw += mw
            x = 1
            break
    listmw.append(mw)
print("Reasonable Bet:", round(totmw/len(listmw)))
# Evidentiate the so-called Saint Petersburg paradox