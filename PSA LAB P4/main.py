# 4. Roulette:
import random
import numpy as np
import matplotlib.pyplot as plt


def casinocolor():
    color = ["Red", "Green", "Black"]
    r = 18 / 38
    b = 18 / 38
    g = 2 / 38
    x = np.random.choice(color, 1, p=[r, g, b])
    return x


def casinonumber():
    l = [0, -1]  # -1 = 00
    for i in range(1, 37):
        l.append(i)
    return random.choice(l)


bet = 20
tot = 20
for game in range(1, 1001):
    tot -= bet
    if casinocolor() == "Red":
        tot += 2 * bet
    else:
        continue
print("Total winnings 1000 bets on red:", tot)

bet2 = 1
tot2 = 1
for game2 in range(1, 1001):
    tot2 -= bet2
    if casinonumber() == 18:
        tot2 += bet2 * 35
    else:
        continue
print("Total winnings 1000 bets on 18:", tot2)
for i in range(1, 4):
    betplt1 = 20
    totplt1 = 20
    gameplt1xaxis = []
    totplt1yaxis = []
    for gameplt1 in range(1, 501):
        gameplt1xaxis.append(gameplt1)
        totplt1yaxis.append(totplt1)
        totplt1 -= betplt1
        if casinocolor() == "Red":
            totplt1 += 2 * betplt1
        else:
            continue
    plt.subplot(3, 2, i)
    plt.plot(gameplt1xaxis, totplt1yaxis)
    plt.title('Total winnings by betting on Red:')
    plt.xlabel('Games')
    plt.ylabel('Total winnings')

for i in range(4, 7):
    betplt2 = 20
    totplt2 = 20
    gameplt2xaxis = []
    totplt2yaxis = []
    for gameplt2 in range(1, 501):
        gameplt2xaxis.append(gameplt2)
        totplt2yaxis.append(totplt2)
        totplt2 -= betplt2
        if casinonumber() == 18:
            totplt2 += 35 * betplt2
        else:
            continue
    plt.subplot(3, 2, i)
    plt.plot(gameplt2xaxis, totplt2yaxis)
    plt.title('Total winnings by betting on 18:')
    plt.xlabel('Games')
    plt.ylabel('Total winnings')
plt.subplots_adjust(top=0.90, bottom=0.11, left=0.125, right=0.9, hspace=0.42,
                    wspace=0.2)
plt.show()
