# 3. Tennis:
import random


def ana():
    l = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    return random.choice(l)


def dan():
    return random.choice([0, 1])


gw = 0
aw = 0
dw = 0
x = int(input("Number of games: ")) + 1
for i in range(1, x):
    aw = 0
    dw = 0
    while aw < 25:
        if ana() == 1:
            aw += 1
        else:
            dw += 1
            if dan() == 1:
                dw += 1
            else:
                aw += 1
    if aw == 25 and dw < 25:
        gw += 1
print("Ana wins with probability:", gw / (x - 1))
