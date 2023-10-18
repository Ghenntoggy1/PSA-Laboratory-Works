# 2. I bet my life on this one:
import random


def choice():
    mychoice = random.randint(1, 6)
    return mychoice


def bullet():
    return random.randint(1, 6)


def difbullet1(bp):
    b1 = random.choice(bp)
    return b1


def difbullet2(bp, b1):
    if b1 != 6 and b1 != 1:
        bp.remove(b1)
        bp.remove(b1 + 1)
        bp.remove(b1 - 1)
    elif b1 == 6:
        bp.remove(b1)
        bp.remove(b1 - 1)
        bp.remove(1)
    elif b1 == 1:
        bp.remove(b1)
        bp.remove(b1 + 1)
        bp.remove(6)
    b2 = random.choice(bp)
    return b2


def c5choice():
    mychoice = random.randint(1, 5)
    return mychoice


def c5bullet():
    return random.randint(1, 5)


def c5difbullet1(bp):
    b1 = random.choice(bp)
    return b1


def c5difbullet2(bp, b1):
    if b1 != 5 and b1 != 1:
        bp.remove(b1)
        bp.remove(b1 + 1)
        bp.remove(b1 - 1)
    elif b1 == 5:
        bp.remove(b1)
        bp.remove(b1 - 1)
        bp.remove(1)
    elif b1 == 1:
        bp.remove(b1)
        bp.remove(b1 + 1)
        bp.remove(5)
    b2 = random.choice(bp)
    return b2


it = int(input("Number of games: "))
print("Probability to stay alive:")
wc = 0
for i in range(1, it + 1):  # 1, it
    bullet1 = bullet()
    if bullet1 == 6:
        bullet2 = 1
    else:
        bullet2 = bullet1 + 1
    x = choice()
    if x != bullet1 and x != bullet2:
        wc += 1
totgames1 = it
print("Probability 6 chamber adjacent spin:", wc/totgames1)  # 4/6

noncorgames = 0
wc2 = 0
for i in range(1, it):
    bullet1 = bullet()
    x = 0
    if bullet1 == 6:
        bullet2 = 1
    else:
        bullet2 = bullet1 + 1
    x1 = choice()
    x = x1 + 1
    if x == 7:
        x = 1
    if x1 == bullet1 or x1 == bullet2:
        noncorgames += 1
        continue
    elif x != bullet1:
        wc2 += 1

totgames2 = it - noncorgames
print("Probability 6 chamber adjacent no spin:", wc2/totgames2)  # 3/4

wc3 = 0
for i in range(1, it):
    bulletspossib = [1, 2, 3, 4, 5, 6]
    bullet1 = difbullet1(bulletspossib)
    bullet2 = difbullet2(bulletspossib, bullet1)
    x = choice()
    if x != bullet1 and x != bullet2:
        wc3 += 1
totgames3 = it
print("Probability 6 chamber non adjacent spin:", wc3/totgames3)  # 4/6

noncorgames2 = 0
wc3 = 0
for i in range(1, it):
    y = 0
    bulletspossib = [1, 2, 3, 4, 5, 6]
    bullet1 = difbullet1(bulletspossib)
    bullet2 = difbullet2(bulletspossib, bullet1)
    x1 = choice()
    y = x1 + 1
    if y == 6:
        y = 1
    if x1 == bullet1 or x1 == bullet2:
        noncorgames2 += 1
        continue
    elif y != bullet1 and y != bullet2:
        wc3 += 1
totgames3 = it - noncorgames2
print("Probability 6 chamber non adjacent no spin:", wc3/totgames3)  # 3/5

wc5c = 0
for i in range(1, it):  # 1, it
    bullet1 = c5bullet()
    if bullet1 == 5:
        bullet2 = 1
    else:
        bullet2 = bullet1 + 1
    x = c5choice()
    if x != bullet1 and x != bullet2:
        wc5c += 1
c5totgames1 = it
print("Probability 5 chamber adjacent spin:", wc5c/c5totgames1)  # 0.6

c5noncorgames = 0
wc2c5 = 0
for i in range(1, it):
    bullet1 = c5bullet()
    x = 0
    if bullet1 == 5:
        bullet2 = 1
    else:
        bullet2 = bullet1 + 1
    x1 = c5choice()
    x = x1 + 1
    if x == 6:
        x = 1
    if x1 == bullet1 or x1 == bullet2:
        c5noncorgames += 1
        continue
    elif x != bullet1 and x != bullet2:
        wc2c5 += 1

c5totgames2 = it - c5noncorgames
print("Probability 5 chamber adjacent no spin:", wc2c5/c5totgames2)  # 0.67

wc3c5 = 0
for i in range(1, it):
    bulletspossib = [1, 2, 3, 4, 5]
    bullet1 = c5difbullet1(bulletspossib)
    bullet2 = c5difbullet2(bulletspossib, bullet1)
    x = c5choice()
    if x != bullet1 and x != bullet2:
        wc3c5 += 1
c5totgames3 = it
print("Probability 5 chamber non adjacent spin:", wc3c5/c5totgames3)  # 0.6

c5noncorgames2 = 0
wc3c5 = 0
for i in range(1, it):
    bulletspossib = [1, 2, 3, 4, 5]
    bullet1 = c5difbullet1(bulletspossib)
    bullet2 = c5difbullet2(bulletspossib, bullet1)
    x = c5choice()
    if x == 5:
        x = 1
    if x == bullet1 or x == bullet2:
        c5noncorgames2 += 1
        continue
    elif x + 1 != bullet1 and x + 1 != bullet2:
        wc3c5 += 1
totgames3c5 = it - c5noncorgames2
print("Probability 5 chamber non adjacent no spin:", wc3c5/totgames3c5)  # 0.33
